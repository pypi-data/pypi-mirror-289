import os
import sys
import ast
import libcst as cst
from libcst.metadata import PositionProvider
import datetime
from typing import List, Any, Dict, Union
from pydantic import BaseModel
import tomli
import tomli_w
import uuid
import enum
import subprocess
from copy import deepcopy
import subprocess_tee
import tempfile
import shutil
from paramit.nb import (
    convert_ipynb_to_py,
    convert_source_code_to_ipynb,
    is_jupyter_kernel_installed,
)
from paramit.constants import YELLOW, MAGENTA, GREEN, RED, RESET

sys.stdout.reconfigure(line_buffering=True)


class ParamitMode(enum.Enum):
    RUN = "run"
    CLOUD = "cloud"
    NOTEBOOK = "notebook"


class ParamitVariable(BaseModel):
    name: str
    value: Any
    type: str
    file_name: str
    line: int
    column: int

    def __str__(self):
        return (
            f"{self.name} = {self.value} ({self.type}) [{self.file_name}:{self.line}]"
        )


class ParamitMetadata(BaseModel):
    version: str
    created_on: str
    script_path: str
    python_path: str


class ParamitParameter(BaseModel):
    name: str
    type: str
    values: List[Any]


class VariableVisitor(cst.CSTVisitor):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.variables = []
        self.current_context = []

    def visit_Assign(self, node: cst.Assign):
        for target in node.targets:
            if isinstance(target.target, cst.Name) and isinstance(
                node.value, cst.Integer
            ):
                pos = self.get_metadata(PositionProvider, node).start
                self.add_variable(
                    target.target.value, node.value.value, pos.line, pos.column
                )
            elif isinstance(target.target, cst.Name) and isinstance(
                node.value, cst.Float
            ):
                pos = self.get_metadata(PositionProvider, node).start
                self.add_variable(
                    target.target.value, node.value.value, pos.line, pos.column
                )
            elif isinstance(target.target, cst.Name) and isinstance(
                node.value, cst.SimpleString
            ):
                pos = self.get_metadata(PositionProvider, node).start
                self.add_variable(
                    target.target.value,
                    node.value.value.strip("'\""),
                    pos.line,
                    pos.column,
                )
            elif isinstance(target.target, cst.Name) and isinstance(
                node.value, cst.Name
            ):
                if node.value.value == "True" or node.value.value == "False":
                    pos = self.get_metadata(PositionProvider, node).start
                    value = True if node.value.value == "True" else False
                    self.add_variable(target.target.value, value, pos.line, pos.column)
            elif (
                isinstance(target.target, cst.Attribute)
                and isinstance(node.value, cst.SimpleString)
                and isinstance(target.target.value, cst.Name)
                and target.target.value.value == "self"
            ):
                pass  # Disabled for now

    def visit_Call(self, node: cst.Call):
        if isinstance(node.func, cst.Name):
            self.current_context.append(node.func.value)
        elif isinstance(node.func, cst.Attribute):
            self.current_context.append(node.func.attr.value)

        # Disabled for now
        """
        for arg in node.args:
            if isinstance(arg, cst.Arg) and isinstance(arg.value, cst.SimpleString):
                self.add_variable(arg.keyword.value if arg.keyword else None, arg.value)
        """

    def leave_Call(self, original_node: cst.Call):
        if self.current_context:
            self.current_context.pop()

    def visit_FunctionDef(self, node: cst.FunctionDef):
        pass
        """
        if node.name.value == "__init__":
            params = node.params
            if params.default_params:
                for param in params.default_params:
                    if isinstance(param.default, cst.SimpleString):
                        pass  # Disabled for now
                        # self.add_variable(param.name.value, param.default)
        """

    def visit_ClassDef(self, node: cst.ClassDef):
        self.current_context.append(node.name.value)
        for base in node.bases:
            if isinstance(base.value, cst.Call):
                self.visit_Call(base.value)

    def leave_ClassDef(self, original_node: cst.ClassDef):
        self.current_context.pop()

    def add_variable(self, name: str, value: Any, line: int, column: int):
        full_name = ".".join(self.current_context + [name]) if name else ""
        self.variables.append(
            ParamitVariable(
                name=full_name,
                value=value,
                type=type(value).__name__,
                file_name=os.path.basename(self.file_path),
                line=line,
                column=column,
            )
        )


class VariableTransformer(cst.CSTTransformer):
    METADATA_DEPENDENCIES = (PositionProvider,)

    ## TODO: Clean all the transformation code
    ## Instead of taking in a config file, this should take in the same
    ## ParamitVariable objects that the VariableVisitor generates
    ## and check against line and column numbers
    def __init__(self, config: Dict[str, Union[str, int, float, bool]]):
        self.config = config

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.Assign:
        if len(original_node.targets) == 1:
            target = original_node.targets[0].target
            if isinstance(target, cst.Name):
                name = target.value
                # pos = self.get_metadata(PositionProvider, original_node).start
                if name in self.config:
                    value = self.config[name]
                    if isinstance(original_node.value, cst.SimpleString):
                        value_node = cst.SimpleString(value=f"'{value}'")
                    elif isinstance(
                        original_node.value, cst.Name
                    ) and original_node.value.value in ["True", "False"]:
                        value_node = cst.Name(value="True" if value else "False")
                    elif isinstance(original_node.value, cst.Integer):
                        value_node = cst.Integer(str(value))
                    elif isinstance(original_node.value, cst.Float):
                        value_node = cst.Float(str(value))
                    else:
                        raise ValueError(f"Unsupported type {type(value)}")
                    return updated_node.with_changes(value=value_node)
        return updated_node


def find_variables(tree: cst.Module, path: str) -> List[ParamitVariable]:
    """Find all variables, their values, and types in the given CST tree."""
    visitor = VariableVisitor(file_path=path)
    wrapper = cst.MetadataWrapper(tree)
    wrapper.visit(visitor)
    return visitor.variables


def expand_paths_in_global_variables(
    global_vars: List[ParamitVariable], script_path: str
) -> List[ParamitVariable]:
    """Expand the path in the given global variables using the script path."""
    expanded_vars = []
    for var in global_vars:
        if isinstance(var.value, str) and var.value != "":
            expanded_path = os.path.abspath(
                os.path.join(os.path.dirname(script_path), var.value)
            )
            if os.path.exists(expanded_path):
                expanded_vars.append(
                    ParamitVariable(
                        name=var.name,
                        value=expanded_path,
                        type=var.type,
                        file_name=var.file_name,
                        line=var.line,
                        column=var.column,
                    )
                )
            else:
                expanded_vars.append(var)
        else:
            expanded_vars.append(var)
    return expanded_vars


def generate_config_file(
    tree: cst.Module,
    path: str,
) -> Dict[str, Any]:
    """Generate a TOML configuration file with the given global variables."""
    global_vars = find_variables(tree, path)
    global_vars = expand_paths_in_global_variables(global_vars, path)
    script_path = path.replace(".toml", ".py")

    config = {"global": {}, "meta": {}}
    for var in global_vars:
        parts = var.name.split(".")
        if len(parts) == 1:
            config["global"][parts[0]] = var.value
        else:
            current_dict = config["global"]
            for part in parts[:-1]:
                if part not in current_dict:
                    current_dict[part] = {}
                current_dict = current_dict[part]
            current_dict[parts[-1]] = var.value

    python_path = get_python_path()

    metadata = ParamitMetadata(
        version="0.2.4",
        created_on=str(datetime.datetime.now()),
        script_path=os.path.abspath(script_path),
        python_path=python_path if python_path else "",
    )

    config["meta"] = metadata.model_dump()

    return config


def load_config_file(path: str) -> dict:
    """Load a TOML configuration file from the given path
    and return it as a dictionary."""

    with open(path, "rb") as f:
        return tomli.load(f)


def set_global_variables_from_config(
    tree: cst.Module, config: Dict[str, Dict[str, Union[str, int, float, bool]]]
) -> cst.Module:
    """Set global variables in the given CST tree using the values from the config dictionary."""
    transformer = VariableTransformer(config["global"])
    wrapper = cst.MetadataWrapper(tree)
    modified_tree = wrapper.visit(transformer)
    return modified_tree


def help_in_args(args: List[str]) -> bool:
    """Check if the help flag is in the given list of arguments."""
    return any(arg in args for arg in ["-h", "--help"])


def parse_args(args: List[str]) -> Dict[str, Any]:
    """Parse the given list of arguments into a dictionary."""
    args_dict = {}
    for arg_index, arg in enumerate(args):
        if arg in ["--help", "--h"]:
            continue
        if arg.startswith("--"):
            if "=" in arg:
                key, value = arg.split("=")
            else:
                key = arg
                if arg_index + 1 >= len(args):
                    print(f"{RED}Error: Argument {arg} is missing a value{RESET}")
                    sys.exit(1)

                value = ""
                while arg_index + 1 < len(args) and not args[arg_index + 1].startswith(
                    "--"
                ):
                    if value:
                        value += ","
                    value += args[arg_index + 1]
                    arg_index += 1

            key = key[2:].replace("-", "_")
            args_dict[key] = value
    return args_dict


def expand_args_dict(args_dict: Dict[str, str]) -> Dict[str, ParamitParameter]:
    """Parse the value in the args according to the special paramit syntax.

    The syntax is as follows:
        "123,126,128" -> [123, 126, 128]
        "blue, red" -> ["blue", "red"]
        "blue red" -> ["blue", "red"]
    """

    hyperparameters = {}
    for arg, value in args_dict.items():
        if "," in value:
            values = value.split(",")
        else:
            values = [value]

        if not values:
            print(f"{RED}Error: Argument {arg} must have at least one value{RESET}")
            sys.exit(1)

        value_type = None
        if all(v.isdigit() for v in values):
            value_type = int
            values = [value_type(v) for v in values]
        elif all(v.replace(".", "").replace("e", "").isdigit() for v in values):
            value_type = float
            values = [value_type(v) for v in values]
        elif all(v.lower() in ["true", "false"] for v in values):
            value_type = bool

            def str_to_bool(value):
                if value.lower() == "true":
                    return True
                elif value.lower() == "false":
                    return False
                else:
                    print(f"{RED}Error: Bool argument must be True or False{RESET}")
                    sys.exit(1)

            values = [str_to_bool(v) for v in values]

        else:
            value_type = str
            values = [value_type(v) for v in values]
            # Make paths absolute if the argument exists as a path
            for i, v in enumerate(values):
                if os.path.exists(v):
                    values[i] = os.path.abspath(v)


        hyperparameters[arg] = ParamitParameter(
            name=arg, type=type(values[0]).__name__, values=values
        )

    return hyperparameters


def pretty_print_config(config: Dict[str, Any]) -> None:
    """Pretty print the config as parameters that can be passed to the CLI."""
    print("Arguments:")
    for key, value in config["global"].items():
        print(f"  --{key.replace('_', '-')}={value}")
    print("\nMetadata:")
    for key, value in config["meta"].items():
        print(f"  {key}: {value}")


def generate_configs_from_hyperparameters(
    base_config: Dict[str, Any], hyperparameters: Dict[str, ParamitParameter]
) -> List[Dict[str, Any]]:
    """Generate a list of configurations from the base config and hyperparameters."""

    hyperparameters_range: List[ParamitParameter] = []
    hyperparameters_single: List[ParamitParameter] = []
    for hyperparameter in hyperparameters:
        if len(hyperparameters[hyperparameter].values) > 1:
            hyperparameters_range.append(hyperparameters[hyperparameter])
        else:
            hyperparameters_single.append(hyperparameters[hyperparameter])

    for hyperparameter in hyperparameters_single:
        if hyperparameter.name in base_config["global"]:
            try:
                base_config["global"][hyperparameter.name] = type(
                    base_config["global"][hyperparameter.name]
                )(hyperparameter.values[0])
            except ValueError:
                print(
                    f"{RED}Error: Argument {hyperparameter.name} must be of type {type(base_config['global'][hyperparameter.name])}{RESET}"
                )
                sys.exit(1)
        else:
            print(
                f"{RED}Error: Argument {hyperparameter.name} not found in the code or config{RESET}"
            )
            # Print the available arguments
            pretty_print_config(base_config)
            sys.exit(1)

    if not hyperparameters_range:
        return [base_config]

    # Generate all possible combinations of hyperparameters
    hyperparameters_combinations = []
    for i in range(len(hyperparameters_range)):
        hyperparameter = hyperparameters_range[i]
        if not hyperparameters_combinations:
            for value in hyperparameter.values:
                hyperparameters_combinations.append({hyperparameter.name: value})
        else:
            new_combinations = []
            for combination in hyperparameters_combinations:
                for value in hyperparameter.values:
                    new_combination = combination.copy()
                    new_combination[hyperparameter.name] = value
                    new_combinations.append(new_combination)
            hyperparameters_combinations = new_combinations

    configs: List[Dict[str, Any]] = []

    for combination in hyperparameters_combinations:
        config = deepcopy(base_config)
        for key, value in combination.items():
            if key in config["global"]:
                try:
                    config["global"][key] = type(config["global"][key])(value)
                except ValueError:
                    print(
                        f"{RED}Error: Argument {key} must be of type {type(config['global'][key])}{RESET}"
                    )
                    sys.exit(1)
            else:
                print(
                    f"{RED}Error: Argument {key} not found in the code or config{RESET}"
                )
                pretty_print_config(base_config)
                sys.exit(1)

        configs.append(config)

    return configs


def print_usage():
    print(
        f"{MAGENTA}Usage: paramit [run | cloud | notebook] <path_to_python_or_toml_file>{RESET}"
    )
    print()
    print("commands")
    print("    run - Run the Python script or notebook")
    print("    cloud - Run the Python script or notebook on the cloud")
    print("    notebook - Start a Jupyter notebook server with the script or notebook")


def get_python_path() -> str:
    # Check a paramit specific environment variable
    if "HAIPERA_PYTHON_PATH" in os.environ:
        return os.environ["HAIPERA_PYTHON_PATH"]

    # Check for VIRTUAL_ENV first (covers venv and conda environments)
    if "VIRTUAL_ENV" in os.environ:
        return os.path.join(os.environ["VIRTUAL_ENV"], "bin", "python")

    # Check for CONDA_PREFIX (specific to conda environments)
    if "CONDA_PREFIX" in os.environ:
        return os.path.join(os.environ["CONDA_PREFIX"], "bin", "python")

    # Look for python3 or python in PATH
    for cmd in ["python3", "python"]:
        python_path = shutil.which(cmd)
        if python_path:
            return python_path

    # If still not found, try common locations
    common_locations = [
        "/usr/bin/python3",
        "/usr/local/bin/python3",
        "/usr/bin/python",
        "/usr/local/bin/python",
        "C:\\Python\\python.exe",
        "C:\\Program Files\\Python\\python.exe",
    ]
    for location in common_locations:
        if os.path.exists(location):
            return location
    raise FileNotFoundError(
        "Could not find a Python interpreter. Please set the HAIPERA_PYTHON_PATH environment variable."
    )


def is_package_installed(package_name: str) -> bool:
    python_path = get_python_path()
    try:
        result = subprocess.run(
            [python_path, "-m", "pip", "show", package_name],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False


def run_code(source_code: str, python_path: str, cwd: str) -> None:
    with tempfile.NamedTemporaryFile("w", delete=False) as temp_file:
        temp_file.write(source_code)
        temp_file_path = temp_file.name

    log_file_path = os.path.join(cwd, "console.log")
    try:
        output = subprocess_tee.run(
            f"{python_path} -u {temp_file_path}",
            cwd=cwd,
            shell=True,
        )

        # Save
        with open(log_file_path, "w") as f:
            f.write(output.stdout)

    except subprocess.CalledProcessError as e:
        return e.stderr
    finally:
        os.unlink(temp_file_path)


def main():
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)

    try:
        mode = ParamitMode(sys.argv[1])
    except ValueError:
        print_usage()
        sys.exit(1)

    mode = ParamitMode(sys.argv[1])

    if mode == ParamitMode.CLOUD:
        print(
            f"{MAGENTA}Cloud runs are in development. Please sign up on the waitlist for updates at https://www.haipera.com{RESET}"
        )
        sys.exit(1)

    path = sys.argv[2]
    if not os.path.exists(path):
        print(f"{RED}Error: File {path} does not exist{RESET}")
        sys.exit(1)

    cli_args = parse_args(sys.argv[3:])
    hyperparameters = expand_args_dict(cli_args)

    if (
        not path.endswith(".py")
        and not path.endswith(".toml")
        and not path.endswith(".ipynb")
    ):
        print(
            f"{RED}Error: File {path} is not a Python or TOML or Notebook file{RESET}"
        )
        sys.exit(1)

    if path.endswith(".toml"):
        config = load_config_file(path)

        try:
            ParamitMetadata(**config["meta"])
        except Exception:
            print(
                f"{RED}Error: The config file is not a valid paramit config file{RESET}"
            )

        if not os.path.exists(config["meta"]["script_path"]):
            print(
                f"{RED}Error: Python file {config['meta']['script_path']} does not exist{RESET}"
            )
            sys.exit(1)

        with open(config["meta"]["script_path"], "r") as f:
            if config["meta"]["script_path"].endswith(".ipynb"):
                code = convert_ipynb_to_py(config["meta"]["script_path"])
            elif config["meta"]["script_path"].endswith(".py"):
                code = f.read()
            else:
                print(
                    f"{RED}Error: Python file {config['meta']['script_path']} is not a Python or Notebook file{RESET}"
                )
                sys.exit(1)

    elif path.endswith(".py"):
        with open(path, "r") as f:
            code = f.read()
    elif path.endswith(".ipynb"):
        code = convert_ipynb_to_py(path)

    try:
        # We do an extra check here to catch syntax errors w/ helpful messages
        ast.parse(code)
    except SyntaxError as e:
        e.filename = path
        print(f"{RED}SyntaxError: {e}{RESET}")
        sys.exit(1)

    tree = cst.parse_module(code)

    config_path = path.replace(".py", ".toml").replace(".ipynb", ".toml")

    if help_in_args(sys.argv[3:]):
        generated_config_file = generate_config_file(tree, path)
        print(f"{MAGENTA}Usage: paramit run <path_to_python_file> [args]{RESET}")
        pretty_print_config(generated_config_file)
        sys.exit(0)

    elif not os.path.exists(config_path):
        generated_config = generate_config_file(tree, path)
        with open(config_path, "wb") as f:
            tomli_w.dump(generated_config, f)

    elif not path.endswith(".toml"):
        print(
            f"{YELLOW}Warning: Configuration file {config_path} already exists{RESET}"
        )
        overwrite = input("Do you want to overwrite it? (y/n): ")
        if overwrite.lower() == "y":
            generated_config = generate_config_file(tree, path)

            with open(config_path, "wb") as f:
                tomli_w.dump(generated_config, f)

    config = load_config_file(config_path)
    python_path = config["meta"]["python_path"]

    experiment_configs = generate_configs_from_hyperparameters(config, hyperparameters)

    if len(experiment_configs) > 100:
        print(f"{YELLOW}Warning: Running {len(experiment_configs)} experiments{RESET}")
        confirm = input("Do you want to continue? (y/n): ")
        if confirm.lower() != "y":
            sys.exit(0)
    elif len(experiment_configs) == 0:
        print(f"{YELLOW}Warning: No experiments to run{RESET}")
        sys.exit(0)
    elif len(experiment_configs) == 1:
        pass
    else:
        print(f"{GREEN}Running {len(experiment_configs)} experiments{RESET}")

    if mode == ParamitMode.NOTEBOOK and len(experiment_configs) > 1:
        print("Notebook mode only supports running a single experiment")
        sys.exit(1)

    for experiment_config in experiment_configs:
        experiment_id = (
            datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            + "-"
            + str(uuid.uuid4())[0:8]
        )
        experiment_dir = os.path.join("reports", experiment_id)
        os.makedirs(experiment_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(path))[0]

        # Save the config file in the experiment directory
        with open(os.path.join(experiment_dir, base_name + ".toml"), "wb") as f:
            tomli_w.dump(experiment_config, f)

        modified_tree = set_global_variables_from_config(tree, experiment_config)

        source_code = modified_tree.code

        if mode == ParamitMode.RUN:
            with open(os.path.join(experiment_dir, base_name + ".py"), "w") as f:
                f.write(source_code)

            if path.endswith(".ipynb"):
                notebook_path = os.path.join(experiment_dir, base_name + ".ipynb")
                with open(notebook_path, "w") as f:
                    f.write(convert_source_code_to_ipynb(source_code))

            print(f"Running with the Python interpreter at {python_path}")
            run_code(source_code, python_path, experiment_dir)

        elif mode == ParamitMode.NOTEBOOK:
            ipykernel_is_installed = is_package_installed("ipykernel")
            if not ipykernel_is_installed:
                print(
                    "ipykernel is not installed. Please install it to use notebook mode"
                )
                sys.exit(1)

            notebook_path = os.path.join(experiment_dir, base_name + ".ipynb")
            with open(notebook_path, "w") as f:
                f.write(convert_source_code_to_ipynb(source_code))
            print("Starting Jupyter notebook server!\n")
            kernel_name = os.path.basename(os.path.dirname(path))
            if not is_jupyter_kernel_installed(kernel_name):
                subprocess.run(
                    [
                        python_path,
                        "-m",
                        "ipykernel",
                        "install",
                        "--name",
                        kernel_name,
                        "--user",
                    ],
                    check=True,
                )
            subprocess.run(
                [
                    "jupyter",
                    "notebook",
                    notebook_path,
                    "--MultiKernelManager.default_kernel_name",
                    kernel_name,
                    "--notebook-dir",
                    experiment_dir,
                ],
                check=True,
            )
