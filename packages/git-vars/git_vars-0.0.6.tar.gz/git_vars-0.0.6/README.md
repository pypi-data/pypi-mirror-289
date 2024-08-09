
## `git-vars` - Manage GitLab Environment Variables with Ease
  

**`git-vars`** is a Python package that simplifies managing GitLab environment variables. It allows you to seamlessly synchronize environment variables between your local machine and GitLab projects. This streamlines your development workflow by ensuring consistency and eliminating the hassle of manual updates.

  

## Installation

  

Install `git-vars` using pip:

  

```bash
pip install  git-vars
```

## Usage

`git-vars` offers three main subcommands: `configure`, `pull`, and `push`.

  

## Pull

Use the pull command to retrieve environment variables from your GitLab project and store them in a local file.

  

```Bash
git-vars pull  -t <access_token> -r <repository_url> [options]
```

  

**Options**:
  

`-s`, `--scope`: (Optional) The scope of environment variables to pull. Valid options are project, group, or instance. If not provided, the scope from the .git-vars file will be used (defaults to project if not set in .git-vars).
  

`-f`, `--file`: (Optional) Path to the file where downloaded variables will be saved. Defaults to `.env`.

  

## Push

Use the push command to update GitLab environment variables from a local file.

  

```Bash
git-vars push  -t <access_token> -r <repository_url> [options]
```

  

**Options**:

`-s`, `--scope`: (Optional) The scope of environment variables to pull. Valid options are project, group, or instance. If not provided, the scope from the .git-vars file will be used (defaults to project if not set in .git-vars).

  

`-f`, `--file`: Path to the file containing environment variables to push. Defaults to `.env`.



## Configure

Use the configure command to create or update the `.git-vars` file with your GitLab access token and repository URL.

```bash
git-vars configure -t <access_token> -r <repository_url>
```

`-t`, `--access-token`: Your GitLab personal access token. This will be saved in the .git-vars file.

  

`-r`, `--repository-url`: The URL of your GitLab repository. This will be saved in the .git-vars file.


`-s`, `--scope`: The scope of environment variables to pull. Valid options are project (default), group, or instance. If not provided, defaults to project.

Example:

  

Pull project environment variables from your GitLab repository and save them to a file named my_env.txt:

```Bash
git-vars pull -f my_env.txt
```

  

Push environment variables defined in local_env.env to your GitLab project's group environment variables:

```Bash
git-vars push -s group -f local_env.env
```

  

## Additional Notes

Make sure you have a personal access token with the necessary permissions created in your GitLab account.

Environment variables are stored in a standard .env file format on your local machine (configurable with `-f` or `--file`).

For detailed information on specific functionalities and error handling, refer to the source code within the package.

