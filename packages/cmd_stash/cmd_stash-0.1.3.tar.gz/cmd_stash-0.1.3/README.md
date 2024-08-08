# Command Stash Tool

A CLI tool for managing and organizing commands with support for saving, listing, exporting, importing, and backing up commands to AWS S3. This tool is designed to help developers quickly store useful commands and retrieve them later, saving time that would otherwise be spent searching through command history.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [Setting Up](#setting-up)
    - [Commands](#commands)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Additional Information](#additional-information)

## Python Versions

This project supports Python versions specified in the `pyproject.toml` file:

```toml
[tool.poetry.dependencies]
python = ">=3.9,<4.0"
```

## Features

- Save commands with categories and descriptions.
- List saved commands with filtering options.
- Import commands from JSON or YAML files.
- Backup commands to Local Storage or AWS S3 bucket.
- Restore commands from an AWS S3 bucket.
- Override and Show Configuration

## Installation

### Using the Makefile

1. **Clone the repository**:

     ```bash
     git clone <repository-url>
     cd <repository-name>
     ```

2. **Run the setup command**:

The Makefile provides a convenient way to set up the project. Run the following command to install dependencies and set up the environment:

     ```bash
     make setup
     ```

     This command will:

     - Install dependencies using poetry.
     - Set up the virtual environment.
     - Install project-specific dependencies.

     If you prefer to set up the environment manually, please refer to the manual setup instructions in the original README.

## Usage

### Setting Up

Configure AWS: Create a config.yaml file in the root directory with the following structure:

```yaml
aws:
    region: your-aws-region
    bucket_name: your-s3-bucket-name
    bucket_privacy: private # or public-read
```

## Commands

### Save a command:
bash
```
cmd_stash save <category> <subcategory> <description> <command>
```

### List all commands
bash
```
cmd_stash list-all
```

### Import a 

### Set the commands file location (optional):
bash```
    cmd_stash set-location <path-to-commands-file>
```


