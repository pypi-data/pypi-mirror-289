"""
Provides functionality related error handling, write and read data.
"""
import requests
from pathlib import Path
import json
from urllib.parse import urlparse
from typing import Dict, Any, List
import configparser


def handle_error_exception(exception: Exception) -> None:
    """
    Handles errors by logging them to the console.

    Args:
    err (Exception): The error to handle
    """
    if isinstance(exception, requests.exceptions.HTTPError):
        print(f"HTTP error occurred: {exception}")
    elif isinstance(exception, requests.exceptions.ConnectionError):
        print(f"Connection error occurred: {exception}")
    elif isinstance(exception, requests.exceptions.Timeout):
        print(f"Timeout error occurred: {exception}")
    elif isinstance(exception, requests.exceptions.RequestException):
        print(f"Request error occurred: {exception}")
    else:
        print(f"An unexpected error occurred: {exception}")
    raise exception

def get_config_value(profile, key):
    """Helper function to get configuration value from the profile in the .git-vars file"""
    config_file_path = Path.home() / ".git-vars"
    config = configparser.ConfigParser()

    # Ensure the configuration file exists and is readable
    if config_file_path.exists():
        config.read(config_file_path)
        if config.has_section(profile):
            return config.get(profile, key)
    
    # Return None if the profile or key is not found
    return None

def get_hostname(url: str) -> str:
    """
    Extracts the protocol and hostname from a URL.

    Args:
    url (str): The URL to parse

    Returns:
    str: The protocol and hostname combined
    """
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"


def format_env_vars(env_vars: List[Dict[str, Any]]) -> str:
    """Env file formating function"""
    return "\n".join([f"{var['key']}={var['value']}" for var in env_vars])


def write_output_to_file(path: str, data: str) -> None:
    """
    Writes data to a file.

    Args:
    path (str): The path to the file
    data (str): The data to write
    """
    with open(path, "w", encoding="utf-8") as f:
        d = format_env_vars(data)
        f.write(d)


def parse_data_from_env(filepath: str) -> Dict[str, Any]:
    """
    Parses environment variables from a file.

    Args:
    filepath (str): The path to the .env file

    Returns:
    Dict[str, Any]: A dictionary of environment variables
    """
    config = configparser.ConfigParser()
    config.optionxform = str  # This preserves case sensitivity

    # Create a temporary file with a section header
    with open(filepath, "r", encoding="utf-8") as original_file:
        content = "[env]\n" + original_file.read()
    config.read_string(content)

    return dict(config["env"])

def get_user_confirmation() -> bool:
    confirmation = input("\nDo you want to apply these changes to GitLab? (yes/no): ")
    return confirmation.lower() in ['yes', 'y']

def display_changes(new_vars, updated_vars, deleted_vars):
    print("\nNew Variables:")
    for var in new_vars:
        print(f"  {var['key']} = {var['value']}")

    print("\nUpdated Variables:")
    for var in updated_vars:
        old_value = var.get('old_value', 'N/A')
        new_value = var['value']
        key = var['key']
        print(f"  {key} --> OLD: {old_value}, NEW: {new_value}")

    print("\nDeleted Variables:")
    for var in deleted_vars:
        print(f"  {var['key']}")

def display_vars(vars, location="remote"):
    try:
        if location == "local":
            print("\nLocal Variables:")
            for key, value in vars.items():
                print(f"  {key} = {value}")
        else:
            print("\nRemote Variables:")
            for var in vars:
                print(f"  {var['key']} = {var['value']}")
    except:
        print("   |   ")
        print("   |   ")
        print("   |   ")
        print("\  |  /")
        print(" \ | / ")
        print("  \|/  ")
        print("       ")
        print("Cannot display the variables.")
        print(vars)