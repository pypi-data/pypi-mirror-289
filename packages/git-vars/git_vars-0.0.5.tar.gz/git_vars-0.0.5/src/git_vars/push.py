"""
Provides functionality related to pushing data to GitLab through the API.
"""

import os
from typing import Dict, Any
import sys
from .utils import parse_data_from_env
from .gitlab_api import GitLabManager

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

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


def get_user_confirmation() -> bool:
    confirmation = input("\nDo you want to apply these changes to GitLab? (yes/no): ")
    return confirmation.lower() in ['yes', 'y']

async def push_vars(options: Dict[str, Any]):
    """
    Async function that uses GitLab Manager class to connect to the GitLab API
    """
    try:
        manager = GitLabManager(
            access_token=options.get("access_token"),
            repository_url=options.get("repository_url"),
            scope=options.get("scope"),
        )

        file = options.get("env_vars")

        # Get env file variables
        if file:
            env_file_vars = parse_data_from_env(file)
        else:
            env_file_vars = parse_data_from_env(".env")

        # Get env variables from GitLab
        gitlab_env_vars = await manager.get_gitlab_env_vars()

        # Synchronize env file variables to GitLab
        updated_env_vars = []
        deleted_env_vars = []
        gitlab_env_var_hashmap = {}

        # Filter updated and deleted env variables
        for env_var in gitlab_env_vars:
            if env_var["key"] in env_file_vars:
                if env_file_vars[env_var["key"]] != env_var["value"]:
                    updated_env_vars.append(
                        {
                            "key": env_var["key"],
                            "old_value": env_var["value"],  # Store old value
                            "value": env_file_vars[env_var["key"]],
                        }
                    )
                del env_file_vars[env_var["key"]]
            else:
                deleted_env_vars.append(
                    {
                        "key": env_var["key"],
                        "value": env_var["value"],
                    }
                )
            gitlab_env_var_hashmap[env_var["key"]] = env_var["value"]

        # Filter new env variables
        new_env_vars = [
            {"key": key, "value": value}
            for key, value in env_file_vars.items()
            if key not in gitlab_env_var_hashmap
        ]

        modified_count = (
            len(new_env_vars) + len(updated_env_vars) + len(deleted_env_vars)
        )

        if modified_count == 0:
            print("Already up to date.")

        else:
            # Display changes to the user
            display_changes(new_env_vars, updated_env_vars, deleted_env_vars)

            # Get user confirmation
            if get_user_confirmation():
                # Perform API operations
                if new_env_vars:
                    await manager.create_gitlab_env_variables(new_env_vars)
                if updated_env_vars:
                    await manager.update_gitlab_env_variables(updated_env_vars)
                if deleted_env_vars:
                    await manager.delete_gitlab_env_variables(deleted_env_vars)

                print("Changes applied successfully.")
            else:
                print("Changes were not applied.")
    

    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise
    except Exception as err:
        print(f"Unexpected error: {err}")
        raise
