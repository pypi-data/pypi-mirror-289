import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class CommandRepository:
    """Command Repository"""

    def __init__(self, file_path: Path):
        self.file_path = Path(file_path)
        self.commands = self.load_commands()

    def validate_structure(self, commands: Dict) -> bool:
        """Validate the structure of the commands dictionary for both JSON and YAML."""

        def is_valid_command_entry(entry):
            """Check if a single command entry has the correct structure."""
            return (
                isinstance(entry, dict)
                and "category" in entry
                and isinstance(entry["category"], str)
                and "subcategory" in entry
                and isinstance(entry["subcategory"], str)
                and "description" in entry
                and isinstance(entry["description"], str)
                and "command" in entry
                and isinstance(entry["command"], str)
            )

        # Check if 'commands' is a top-level key and it is a list
        if isinstance(commands, dict):
            if "commands" in commands:
                commands_list = commands["commands"]
                if isinstance(commands_list, list):
                    return all(is_valid_command_entry(item) for item in commands_list)

        # Otherwise, handle the case where commands is a dictionary with category-subcategory structure
        if isinstance(commands, dict):
            for category, subcategories in commands.items():
                if not isinstance(category, str) or not isinstance(subcategories, dict):
                    return False

                if (
                    not subcategories
                ):  # Ensure each category has at least one sub-category
                    return False

                for subcategory, command_dict in subcategories.items():
                    if not isinstance(subcategory, str) or not isinstance(
                        command_dict, dict
                    ):
                        return False

                    if (
                        not command_dict
                    ):  # Ensure each sub-category has at least one command
                        return False

                    for description, command in command_dict.items():
                        if not isinstance(description, str) or not isinstance(
                            command, str
                        ):
                            return False

            return True

    def load_commands(self) -> Dict[str, Any]:
        """Load commands from a file based on its extension."""
        if self.file_path.exists():
            try:
                logger.debug("Loading commands from %s", self.file_path)

                with open(self.file_path, "r", encoding="utf-8", errors="replace") as f:
                    file_content = f.read().strip()  # Read and strip whitespace

                    if not file_content:  # Check if the file is empty
                        logger.debug("File is empty")
                        return {}

                    if self.file_path.suffix == ".json":
                        data = json.loads(
                            file_content
                        )  # Use loads to handle string content
                        logger.debug("Loaded JSON data %s", data)
                        if isinstance(data, dict):
                            return data
                        else:
                            logger.error("JSON data is not a dictionary")
                            raise ValueError("JSON data is not a dictionary")

                    elif self.file_path.suffix in [".yaml", ".yml"]:
                        data = yaml.safe_load(
                            file_content
                        )  # Use safe_load for string content
                        logger.debug("Loaded YAML data %s", data)
                        if isinstance(data, dict):
                            return data
                        else:
                            logger.error("YAML data is not a dictionary")
                            raise ValueError("YAML data is not a dictionary")

                    else:
                        logger.error(
                            "Unsupported file extension %s", self.file_path.suffix
                        )
                        raise ValueError("Unsupported file extension")

            except json.JSONDecodeError as e:
                logger.error("JSON decode error: %s", e)
                raise
            except yaml.YAMLError as e:
                logger.error("YAML load error: %s", e)
                raise
            except Exception as e:
                logger.error("Failed to load commands from %s: %s", self.file_path, e)
                raise
        else:
            logger.debug("File does not exist %s", self.file_path)
        return {}  # Ensure that we always return a dictionary

    def save_commands(self):
        """Save commands to a file based on its extension."""
        try:
            if self.file_path.suffix == ".json":
                with open(self.file_path, "w", encoding="utf-8") as f:
                    json.dump(self.commands, f, indent=2)
            elif self.file_path.suffix in [".yaml", ".yml"]:
                with open(self.file_path, "w", encoding="utf-8") as f:
                    yaml.dump(self.commands, f, default_flow_style=False)
        except Exception as e:
            logger.error("Failed to save commands to %s %s", self.file_path, e)
            raise

    def save_command(self, category, subcategory, description, command):
        """Save a single command into the repository."""
        if category not in self.commands:
            self.commands[category] = {}
        if subcategory not in self.commands[category]:
            self.commands[category][subcategory] = {}
        self.commands[category][subcategory][description] = command
        self.save_commands()
        logger.info(
            "Saved command under category %s, subcategory %s with description %s",
            category,
            subcategory,
            description,
        )
        return "Saved command: %s" % command

    def list_commands(self, category, subcategory=None, description=None):
        """List commands filtered by category, subcategory, and description."""
        result = {}

        if category in self.commands:
            category_data = self.commands[category]

            if subcategory:
                if subcategory in category_data:
                    subcategory_data = category_data[subcategory]
                    result = {subcategory: subcategory_data}
                else:
                    result = {}
            else:
                result = category_data

            if description:
                result = {
                    k: {d: c for d, c in v.items() if d == description}
                    for k, v in result.items()
                }
        return result

    def list_all_commands(self):
        """List all commands."""
        return self.commands

    def list_categories(self) -> list:
        """List all top-level categories."""
        return list(self.commands.keys())

    def export_commands(self, file_path: Path):
        """Export commands to a file based on its extension."""
        try:
            if file_path.suffix == ".json":
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(self.commands, f, indent=2)
            elif file_path.suffix in [".yaml", ".yml"]:
                with open(file_path, "w", encoding="utf-8") as f:
                    yaml.dump(self.commands, f, default_flow_style=False)
            logger.info("Commands exported to %s", file_path)
        except Exception as e:
            logger.error("Failed to export commands to %s: %s", file_path, e)
            raise

    def import_commands(self, file_path: Path):
        """Import commands from a file based on its extension."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                if file_path.suffix == ".json":
                    imported_commands = json.load(f)
                elif file_path.suffix in [".yaml", ".yml"]:
                    imported_commands = yaml.safe_load(f)
                else:
                    raise ValueError(
                        "Unsupported file format. Use '.json', '.yaml', or '.yml'."
                    )

            # Validate the structure of the imported commands
            if not self.validate_structure(imported_commands):
                raise ValueError("Invalid commands schema")

            self.commands.update(imported_commands)
            self.save_commands()
            logger.info("Commands imported from %s", file_path)
            return "Commands successfully imported from %s" % file_path

        except json.JSONDecodeError:
            logger.error("Failed to import commands from %s: Invalid JSON", file_path)
            raise
        except UnicodeDecodeError:
            error_message = (
                "Encoding error while importing commands from %s" % file_path
            )
            logger.error(error_message)
            return error_message
        except ValueError as ve:
            error_message = str(ve)
            logger.error(
                "Failed to import commands from %s %s", file_path, error_message
            )
            raise  # Ensure that ValueError is raised for invalid schema
        except Exception as e:
            error_message = "Failed to import commands from %s: %s" % (file_path, e)
            logger.error(error_message)
            return error_message

    def remove_commands(
        self,
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        key: Optional[str] = None,
    ) -> str:
        """Remove commands from the repository.
        - If `category`, `subcategory`, and `key` are provided, remove the specific command.
        - If `category` and `subcategory` are provided, remove all commands in that subcategory.
        - If only `category` is provided, remove all commands under that category.
        - If no arguments are provided, remove all commands.
        """
        if category is None:
            # Remove all commands
            if self.commands:
                self.commands.clear()
                self.save_commands()
                logger.info("All commands have been removed.")
                return "All commands have been removed."

        else:
            if category not in self.commands:
                logger.error("Category '%s' not found.", category)
                raise ValueError("Category '%s' not found." % category)

            if subcategory is None:
                # Remove all commands under the specified category
                del self.commands[category]
                self.save_commands()
                logger.info("Removed all commands under category '%s'.", category)
                return "All commands under category '%s' have been removed." % category

            if subcategory not in self.commands[category]:
                logger.error(
                    "Subcategory '%s' not found in category '%s'.",
                    subcategory,
                    category,
                )
                raise ValueError(
                    "Subcategory '%s' not found in category '%s'."
                    % (subcategory, category)
                )

            if key is None:
                # Remove all commands under the specified subcategory
                del self.commands[category][subcategory]
                if not self.commands[category]:  # Remove category if empty
                    del self.commands[category]
                self.save_commands()
                logger.info(
                    "Removed all commands under subcategory '%s' in category '%s'.",
                    subcategory,
                    category,
                )
                return (
                    "All commands under subcategory '%s' in category '%s' have been removed."
                    % (subcategory, category)
                )

            if key not in self.commands[category][subcategory]:
                logger.error(
                    "Key '%s' not found in subcategory '%s' under category '%s'.",
                    key,
                    subcategory,
                    category,
                )
                raise ValueError(
                    "Key '%s' not found in subcategory '%s' under category '%s'."
                    % (key, subcategory, category)
                )

            # Remove a specific command
            del self.commands[category][subcategory][key]
            if not self.commands[category][subcategory]:  # Remove subcategory if empty
                del self.commands[category][subcategory]
                if not self.commands[category]:  # Remove category if empty
                    del self.commands[category]
            self.save_commands()
            logger.info(
                "Removed command with key '%s' from subcategory '%s' in category '%s'.",
                key,
                subcategory,
                category,
            )
            return (
                "Command with key '%s' from subcategory '%s' in category '%s' has been removed."
                % (key, subcategory, category)
            )
        return ""  # Add a return statement at the end of the function
