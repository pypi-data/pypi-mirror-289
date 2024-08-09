import json
import logging
from pathlib import Path
from typing import Optional

import click
import yaml

from cmd_assist.backup_factory import BackupFactory
from cmd_assist.backup_service import (BackupCreationException,
                                       BackupDestructionException)
from cmd_assist.command_repository import CommandRepository
from cmd_assist.configuration.config_manager import ConfigManager
from cmd_assist.logging_config import setup_logging

# Set up logging
setup_logging(level=logging.DEBUG, log_to_file=True, log_file="cmd_assist.log")
logger = logging.getLogger(__name__)


class CLIManager:
    """CLI Manager to handle command line interactions."""

    def __init__(self, config_path: Optional[Path] = None):
        if config_path:
            # Initialize ConfigManager with the provided configuration path
            self.config_manager = ConfigManager.get_instance(settings_path=config_path)
        else:
            # Use singleton pattern with default settings
            self.config_manager = ConfigManager.get_instance()
        self.settings = self.config_manager.get_settings()
        self.backup_service = BackupFactory.get_instance()
        self.location = self.settings.commands_file
        self.resource_name = self.config_manager.get_resource_name()
        self.object_name = self.settings.object_name
        self.initialize_location(self.location)
        self.cli = click.Group()

        # Register commands
        self.cli.add_command(self.set_config())
        self.cli.add_command(self.show_config())
        self.cli.add_command(self.export_config())
        self.cli.add_command(self.show_bundles())
        self.cli.add_command(self.save_command())
        self.cli.add_command(self.list_commands())
        self.cli.add_command(self.list_all_commands())
        self.cli.add_command(self.list_categories())
        self.cli.add_command(self.import_commands())
        self.cli.add_command(self.create_backup())
        self.cli.add_command(self.destroy_backup())
        self.cli.add_command(self.remove())
        self.cli.add_command(self.backup())
        self.cli.add_command(self.fetch())
        self.cli.add_command(self.restore())

    def initialize_location(self, location):
        """Ensure the location path exists and create it if necessary."""
        path = Path(location)
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        return str(path)

    def set_config(self):
        """Set or update the path to the configuration file."""

        @click.command(name="set-config")
        @click.argument(
            "config", type=click.Path(exists=True, dir_okay=False, file_okay=True)
        )
        def set_config_command(config):
            config_path = Path(config).resolve()

            if not config_path.is_absolute():
                click.echo(f"Error: The path '{config_path}' is not an absolute path.")
                raise click.UsageError("Please provide an absolute path.")

            # Update the configuration path in the settings
            try:
                settings = self.config_manager.get_settings()
                settings.config_path = config_path
                self.config_manager.save_settings()  # Save settings with the new config path
                click.echo(f"Configuration path updated to: {config_path}")
            except FileNotFoundError as e:
                click.echo(f"Error: File not found - {e}")
                logger.error("File not found error: %s", e)
            except IOError as e:
                click.echo(f"Error: I/O error - {e}")
                logger.error("I/O error: %s", e)
            except ValueError as e:
                click.echo(f"Error: Value error - {e}")
                logger.error("Value error: %s", e)
            except Exception as e:
                click.echo(f"Error: Unexpected error - {e}")
                logger.error("Unexpected error: %s", e)

        return set_config_command

    def show_config(self):
        """Display the current configuration details."""

        @click.command(name="show-config")
        def show_config_command():
            config_details = self.config_manager.get_configuration_details()
            path_location = self.config_manager.get_config_location()
            if config_details:
                click.echo(f"Configuration path: {path_location}")
                click.echo("Configuration details:")
                click.echo(json.dumps(config_details, indent=2))
            elif self.config_manager.default_config_path.exists():
                config = self.config_manager.load_yaml_config(
                    self.config_manager.default_config_path
                )
                click.echo(
                    f"Using default configuration from {self.config_manager.default_config_path}"
                )
                click.echo(json.dumps(config, indent=2))
            else:
                click.echo("Using default configuration.")
                click.echo(json.dumps({"default": "config"}, indent=2))

        return show_config_command

    def export_config(self):
        """Export the current configuration to a file."""

        @click.command(name="export-config")
        @click.argument("output_file", type=click.Path(dir_okay=False, file_okay=True))
        def export_config_command(output_file):
            output_path = Path(output_file).resolve()

            if not output_path.is_absolute():
                click.echo(f"Error: The path '{output_path}' is not an absolute path.")
                raise click.UsageError("Please provide an absolute path.")

            try:
                self.config_manager.export_settings(output_path)
                click.echo(f"Configuration exported to: {output_path}")
            except RuntimeError as e:
                click.echo(f"Error exporting configuration: {e}")
                logger.error("Error exporting configuration: %s", e)

        return export_config_command

    def show_bundles(self):
        """Show a list of available bundles."""

        @click.command(name="show-bundles")
        def show_bundles_command():
            try:
                bundle_names = self.config_manager.get_bundle_names()
                if bundle_names:
                    click.echo("Available bundles:")
                    for name in bundle_names:
                        click.echo(f"- {name}")
                else:
                    click.echo("No bundles available.")
            except RuntimeError as e:
                click.echo(f"Error: {e}")
                logger.error("Error showing bundles: %s", e)

        return show_bundles_command

    def remove(self):
        """Remove all/category/sub-category/specific commands from the current location."""

        @click.command(name="remove")
        @click.option(
            "--category", default=None, help="Category to remove commands from."
        )
        @click.option(
            "--subcategory", default=None, help="Subcategory to remove commands from."
        )
        @click.option(
            "--description",
            default=None,
            help="Specific command description to remove.",
        )
        @click.confirmation_option(
            prompt="Are you sure you want to remove the commands? This action cannot be undone."
        )
        def remove_command(category, subcategory, description):
            """Command function to remove commands based on provided parameters."""
            try:
                cmd_repo = CommandRepository(file_path=self.location)
                cmd_repo.remove_commands(category, subcategory, description)
                if description:
                    click.echo(f"Command with description '{description}' removed.")
                elif subcategory:
                    click.echo(
                        f"All commands in subcategory '{subcategory}' have been removed."
                    )
                elif category:
                    click.echo(
                        f"All commands in category '{category}' have been removed."
                    )
                else:
                    click.echo(f"All commands have been removed from {self.location}.")
            except Exception as e:
                click.echo(f"Error: {e}")
                logger.error("Error removing commands from %s: %s", self.location, e)

        return remove_command

    def fetch(self):
        """Fetch commands for specified bundles."""

        @click.command(name="fetch")
        @click.argument("bundle_names", nargs=-1)
        @click.option(
            "--destination",
            default="fetched",
            help="Destination folder for downloaded commands.",
        )
        def fetch_command(bundle_names, destination):
            if not bundle_names:
                click.echo("Error: No bundle names provided.")
                return

            config_manager = ConfigManager.get_instance()
            for bundle_name in bundle_names:
                bundle_url = config_manager.get_bundle_url(bundle_name)
                if not bundle_url:
                    click.echo(f"Error: Bundle '{bundle_name}' not found.")
                    continue

                try:
                    result = self.config_manager.fetch_bundle(bundle_url, destination)
                    click.echo(result)
                    # Define the path to the fetched file
                    fetched_file_path = (
                        Path(destination) / f"{bundle_name}_commands.json"
                    )

                    # Check if the file exists before trying to import
                    if fetched_file_path.is_file():
                        # Import the fetched commands
                        cmd_repo = CommandRepository(file_path=self.location)
                        import_result = cmd_repo.import_commands(fetched_file_path)
                        click.echo(import_result)

                    else:
                        click.echo(
                            f"Error: Fetched file {fetched_file_path} does not exist."
                        )
                except RuntimeError as e:
                    click.echo(f"Error: {e}")

        return fetch_command

    def save_command(self):
        """Save a command with the given category, subcategory, and description."""

        @click.command(name="save")
        @click.argument("category")
        @click.argument("subcategory")
        @click.argument("description")
        @click.argument("command", nargs=-1)
        def save_command(category, subcategory, description, command):
            cmd_repo = CommandRepository(file_path=self.location)
            try:
                command_str = " ".join(command)
                result = cmd_repo.save_command(
                    category, subcategory, description, command_str
                )
                click.echo(f"Saved command: {result}")
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error saving command: %s", e)

        return save_command

    def list_commands(self):
        """List all commands under a category, optionally filtered by subcategory and description."""

        @click.command(name="list")
        @click.argument("category")
        @click.argument("subcategory", default=None, required=False)
        @click.option("--description", default=None, help="Filter by description")
        def list_commands_command(category, subcategory, description):
            cmd_repo = CommandRepository(file_path=self.location)
            try:
                result = cmd_repo.list_commands(category, subcategory, description)
                click.echo(json.dumps(result, indent=2))
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error listing commands: %s", e)

        return list_commands_command

    def list_all_commands(self):
        """List all commands."""

        @click.command(name="list-all")
        def list_all_commands_command():
            cmd_repo = CommandRepository(file_path=self.location)
            try:
                result = cmd_repo.list_all_commands()
                click.echo(json.dumps(result, indent=2))
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error listing commands: %s", e)

        return list_all_commands_command

    def list_categories(self):
        """List all top-level categories from the current location."""

        @click.command(name="list-categories")
        def list_categories_command():
            """Command function to list all categories."""
            try:
                cmd_repo = CommandRepository(file_path=self.location)
                categories = cmd_repo.list_categories()
                if categories:
                    click.echo("Categories:")
                    for category in categories:
                        click.echo(f"- {category}")
                else:
                    click.echo("No categories found.")
            except RuntimeError as e:
                click.echo(f"Error: {e}")
                logger.error("Error listing categories from %s: %s", self.location, e)

        return list_categories_command

    def import_commands(self):
        """Import commands from a JSON or YAML file."""

        @click.command(name="import")
        @click.argument("file_path", type=click.Path(dir_okay=False, file_okay=True))
        def import_commands_command(file_path):
            file_path = Path(file_path)
            if not file_path.is_file():
                click.echo(
                    f"Error: The file {file_path} does not exist or is not a valid file."
                )
                logger.error(
                    "File %s does not exist or is not a valid file.", file_path
                )
                return
            try:
                cmd_repo = CommandRepository(file_path=self.location)
                cmd_repo.import_commands(file_path)
                click.echo(f"Commands imported from {file_path}")
            except (OSError, IOError, json.JSONDecodeError, yaml.YAMLError) as e:
                click.echo(f"Error importing commands: {e}")
                logger.error("Error importing commands from %s: %s", file_path, e)
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error importing commands: %s", e)

        return import_commands_command

    def create_backup(self):
        """Create a backup."""

        @click.command(name="create-backup")
        def create_backup_command():
            try:
                result = self.backup_service.create_backup(self.resource_name)
                click.echo(result)
            except BackupCreationException as e:
                click.echo(f"Error creating backup: {e}")
                logger.error("Error creating backup: %s", e)
            except Exception as e:
                click.echo(f"Unexpected error: {e}")
                logger.error("Unexpected error: %s", e)

        return create_backup_command

    def destroy_backup(self):
        """Destroy a backup."""

        @click.command(name="destroy-backup")
        @click.argument("resource_name")
        @click.confirmation_option(
            prompt="Are you sure you want to destroy the backup?"
        )
        def destroy_backup_command(resource_name):
            """Command function to destroy the backup."""
            try:
                result = self.backup_service.destroy_backup(resource_name)
                click.echo(result)
            except BackupDestructionException as e:
                click.echo(f"Error destroying backup: {e}")
                logger.error("Error destroying backup: %s", e)
            except Exception as e:
                click.echo(f"Unexpected error: {e}")
                logger.error("Unexpected error: %s", e)

        return destroy_backup_command

    def backup(self):
        """Backup a file."""

        @click.command(name="backup")
        def backup_command():
            if not self.backup_service.backup_exists(self.resource_name):
                click.echo(
                    f"Error: The backup resource '{self.resource_name}' does not exist."
                )
                logger.warning(
                    "Backup resource '%s' does not exist.", self.resource_name
                )
                return
            try:
                result = self.backup_service.backup(
                    self.location, self.resource_name, self.object_name
                )
                click.echo(result)
            except Exception as e:
                click.echo(f"Error during backup: {e}")
                logger.error("Error during backup: %s", e)

        return backup_command

    def restore(self):
        """Restore a file."""

        @click.command(name="restore")
        @click.confirmation_option(
            prompt="Are you sure you want to restore the backup?"
        )
        def restore_command():
            if not self.backup_service.backup_exists(self.resource_name):
                click.echo(
                    f"Error: The backup resource '{self.resource_name}' does not exist."
                )
                logger.warning(
                    "Backup resource '%s' does not exist.", self.resource_name
                )
                return
            try:
                result = self.backup_service.restore(
                    self.resource_name, self.object_name, self.location
                )
                click.echo(result)
            except Exception as e:
                click.echo(f"Error during restore: {e}")
                logger.error("Error during restore: %s", e)

        return restore_command


def cli():
    """Entry point for the CLI commands."""
    setup_logging(level=logging.DEBUG, log_to_file=True)

    cli_manager = CLIManager()
    cli_manager.cli()


if __name__ == "__main__":
    cli()
