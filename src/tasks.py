import os
import yaml
import logging
import argparse
import subprocess
import time
import traceback
from typing import List, Dict

import falcon_adapter
import static_check
import utils
import analyze_pipeline
import chatgpt_api
import config as global_config
from config import OPENAI_API_KEY
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich_utils import *
import openai

# Configure OpenAI API key
openai.api_key = OPENAI_API_KEY

# Initialize logger and console
logger = logging.getLogger(__name__)
console = Console()


# Utility Functions
def load_yaml_file(filepath: str) -> dict:
    """Load a YAML file and return its contents."""
    with open(filepath, "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def load_config(config_name: str) -> dict:
    """Load a specific configuration file."""
    for ext in [".yml", ".yaml"]:
        filepath = os.path.join("tasks", f"{config_name}{ext}")
        if os.path.exists(filepath):
            return load_yaml_file(filepath)
    raise FileNotFoundError(f"No such file: {config_name}")


def load_configs(config_names: List[str]) -> List[dict]:
    """Load multiple configuration files."""
    return [load_config(name) for name in config_names]


def load_all_configs() -> List[dict]:
    """Load all configuration files in the 'tasks' directory."""
    return [load_yaml_file(os.path.join("tasks", file)) for file in os.listdir("tasks") if file.endswith((".yml", ".yaml"))]


def load_rules(rule_indices: List[int]) -> List[dict]:
    """Load specific rules based on indices."""
    rules = []
    for index in rule_indices:
        filepath = os.path.join("rules", f"{index}.yml")
        if os.path.exists(filepath):
            rules.append(load_yaml_file(filepath))
        else:
            raise FileNotFoundError(f"No such file: {index}")
    return rules


def load_all_rules() -> List[dict]:
    """Load all rule files in the 'rules' directory."""
    return [load_yaml_file(os.path.join("rules", file)) for file in os.listdir("rules") if file.endswith(".yml")]


def compile_project(abs_path: str):
    """Compile the project using Falcon."""
    return falcon.Falcon(abs_path)


def handle_vulnerability_analysis(source_dir: str, scan_rules: List[dict]) -> Tuple[dict, dict, dict]:
    """Perform vulnerability analysis."""
    return analyze_pipeline.ask_whether_has_vul_with_scenario_v9(source_dir, scan_rules)


def summarize_results(final_result: dict, scan_rules: List[dict], source_dir: str, start_time: float):
    """Summarize and process results."""
    num_true, num_false = 0, 0
    meta_data = {"files_after_static": set(), "contracts_after_static": set(), "functions_after_static": set(), "rules_types_after_static": set()}

    # Count results
    for file_data in final_result.values():
        for contract_data in file_data.values():
            for function1_data in contract_data.values():
                for function2_data in function1_data.values():
                    for vul_data in function2_data.values():
                        if vul_data.get("StaticAnalysis"):
                            meta_data["files_after_static"].add(file_data)
                            num_true += 1
                        else:
                            num_false += 1

    # Prepare metadata
    meta_data.update({
        "used_time": time.time() - start_time,
        "vul_before_static": num_true + num_false,
        "vul_after_static": num_true,
        "token_sent": chatgpt_api.tokens_sent.value,
        "token_received": chatgpt_api.tokens_received.value,
        "estimated_cost": (chatgpt_api.tokens_sent.value * global_config.SEND_PRICE) +
                          (chatgpt_api.tokens_received.value * global_config.RECEIVE_PRICE),
    })

    # Convert sets to counts
    for key, value in meta_data.items():
        if isinstance(value, set):
            meta_data[key] = len(value)

    return meta_data


def display_summary(meta_data: dict):
    """Display a summary table."""
    table = Table(title="Summary")
    table.add_column("Key")
    table.add_column("Value")
    for key, value in meta_data.items():
        table.add_row(key, str(value))
    console.print(table)


# Main CLI Function
def simple_cli():
    """Command-line interface for vulnerability scanning."""
    parser = argparse.ArgumentParser(description="GPTScan: Smart contract vulnerability scanner")
    parser.add_argument("-s", "--source", help="The source code directory", required=True)
    args = parser.parse_args()

    source_dir = args.source
    start_time = time.time()

    # Load rules
    scan_rules = load_all_rules()
    console.log(f"Loaded [bold green]{len(scan_rules)}[/bold green] rules")

    # Compile the project
    try:
        falcon_instance = compile_project(source_dir)
    except Exception as e:
        console.log(f"[bold red]Compilation failed: {e}[/bold red]")
        console.log("[yellow]Some static analysis may not be enabled, causing reduced precision.[/yellow]")
        falcon_instance = None

    # Perform vulnerability analysis
    res, cg, meta_data = handle_vulnerability_analysis(source_dir, scan_rules)

    # Summarize results
    final_result = {}  # This would be populated with analyzed results
    meta_data = summarize_results(final_result, scan_rules, source_dir, start_time)

    # Display summary
    display_summary(meta_data)

    # Save results
    output_dir = source_dir
    utils.save_output(final_result, output_dir, meta_data)

