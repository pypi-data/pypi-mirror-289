"""
Main section where parsing of the package 'gitlab-variables' is done.
This script provides a command-line interface (CLI) for managing GitLab environment variables.
It utilizes Click for command-line argument parsing and asyncio for asynchronous operations.
"""

import asyncio
import click
import logging
import configparser
from pathlib import Path
from .utils import handle_error_exception, get_config_value
from .push import push_vars
from .pull import pull_vars

# Set up a logger for the module
logger = logging.getLogger(__name__)

def setup_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.debug(f'Logging set to {"DEBUG" if verbose else "INFO"} level')

@click.group()
@click.version_option(version="0.1", prog_name="env-vars")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose mode for detailed output")
def cli(verbose):
    """GitLab environment variable management pip package"""
    setup_logging(verbose)
    logger.debug("Verbose mode enabled")


@cli.command()
@click.option("-p", "--profile", default="default", help="Configuration profile to use")
@click.option(
    "-s",
    "--scope",
    type=click.Choice(["project", "group", "instance"]),
    default="project",
    help="Scope of environment variables: project | group | instance (default: project)",
)
@click.option("-f", "--file", help="Output file")
def pull(profile, scope, file):
    """Pull GitLab repo environment variables to file"""
    # Create a dictionary to store command-line arguments
    access_token = get_config_value(profile, 'access_token')
    repository_url = get_config_value(profile, 'repository_url')
    scope = scope or get_config_value(profile, 'scope')

    if not access_token or not repository_url:
        click.echo("Access token or repository URL not provided. Please run `git-vars configure` to set them.")
        return
    
    vars_dict = {
        "access_token": access_token,
        "repository_url": repository_url,
        "scope": scope,
        "output_file": file,
    }
    logger.debug(f'Pull command called with args: {vars_dict}')
    try:
        asyncio.run(pull_vars(vars_dict))
    except Exception as err:
        logger.error(f'Error in pull command: {err}')
        handle_error_exception(err)

@cli.command()
@click.option("-p", "--profile", default="default", help="Configuration profile to use")
@click.option(
    "-s", "--scope",
    type=click.Choice(["project", "group", "instance"]),
    default="project",
    help="Scope of environment variables: project | group | instance (default: project)",
)
@click.option("-f", "--file", help="Environment variables file")
def push(profile, scope, file):
    """Push GitLab repo environment variables to file"""
    # Create a dictionary to store command-line arguments
    access_token = get_config_value(profile, 'access_token')
    repository_url = get_config_value(profile, 'repository_url')

    if not access_token or not repository_url:
        click.echo("Access token or repository URL not provided. Please run `git-vars configure` to set them.")
        return
    
    vars_dict = {
        "access_token": access_token,
        "repository_url": repository_url,
        "scope": scope,
        "env_vars": file,
    }
    
    logger.debug(f'Push command called with args: {vars_dict}')
    try:
        asyncio.run(push_vars(vars_dict))
    except Exception as err:
        logger.error(f'Error in push command: {err}')
        handle_error_exception(err)

@cli.command()
@click.option("-t", "--access-token", prompt="GitLab access token", help="GitLab access token")
@click.option("-r", "--repository-url", prompt="GitLab repository URL", help="GitLab repository URL")
@click.option(
    "-s", "--scope",
    prompt="GitLab scope (project | group | instance)",
    type=click.Choice(["project", "group", "instance"]),
    default="project",
    help="Scope of environment variables: project | group | instance (default: project)",
)
@click.option("-p", "--profile", default="default", help="Configuration profile to use")
def configure(access_token, repository_url, scope, profile):
    """Configure GitLab settings and store in .git-vars file"""
    config_file_path = Path.home() / ".git-vars"
    config = configparser.ConfigParser()
    
    if config_file_path.exists():
        config.read(config_file_path)
    
    if not config.has_section(profile):
        config.add_section(profile)

    config[profile]['access_token'] = access_token
    config[profile]['repository_url'] = repository_url
    config[profile]['scope'] = scope

    
    try:
        with config_file_path.open('w') as config_file:
            config.write(config_file)
        print(f"Configuration saved to {config_file_path}")
    except IOError as e:
        logger.error(f"Failed to write configuration file: {e}")
        handle_error_exception(e)

def main():
    """Main function that runs the cli()"""
    cli()

if __name__ == "__main__":
    main()
