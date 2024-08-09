"""
Provides functionality related to pushing data to GitLab through the API.
"""

from typing import Dict, Any
from .utils import parse_data_from_env, display_vars
from .gitlab_api import GitLabManager
from pathlib import Path


async def listLocalVars(filepath=None):
    """
    Async function that uses GitLab Manager class to connect to the GitLab API
    """
    try:

        # Get env file variables
        if filepath:
            file_path = Path(filepath)
            if not file_path.is_absolute():
                file_path = Path.cwd() / filepath
            print(f"Getting variables from: {file_path}")
        else:
            file_path = Path.cwd() / ".env"
            print(f"Getting variables from: {file_path}")

        env_file_vars = parse_data_from_env(file_path)
        display_vars(env_file_vars, location="local")

    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise
    except Exception as err:
        print(f"Unexpected error: {err}")
        raise

async def listRemoteVars(options: Dict[str, Any]):
    """
    Async function that uses GitLab Manager class to connect to the GitLab API
    """

    try:
        manager = GitLabManager(
            access_token=options.get("access_token"),
            repository_url=options.get("repository_url"),
            scope=options.get("scope"),
        )

        env_vars = await manager.get_gitlab_env_vars()
        display_vars(env_vars, location="remote")

    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise
    except Exception as err:
        print(f"Unexpected error: {err}")
        raise
