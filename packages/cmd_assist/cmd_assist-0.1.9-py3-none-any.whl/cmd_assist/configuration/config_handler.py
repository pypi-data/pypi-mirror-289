import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from yaml import YAMLError

from cmd_assist.configuration.models import AppSettings
from cmd_assist.file_utils import FileUtils

# Configure logging
logger = logging.getLogger(__name__)

# Constants for default values
DEFAULT_COMMANDS_FILE = "commands.json"
DEFAULT_BACKUP_PROVIDER = "local"
DEFAULT_OBJECT_NAME = "commands.json"
DEFAULT_DIRECTORY = "~/.cmd_assist"
DEFAULT_DIRECTORY_NAME = "backups"

# Define the type for a single bundle
BundleType = Dict[str, str]

# Define the type for the list of bundles
DEFAULT_BUNDLES: List[BundleType] = []


class ConfigHandler:
    """Handles loading, saving, and exporting configuration files."""

    def __init__(self, settings_path: Optional[Path] = None) -> None:
        self.settings_path = settings_path or (
            Path.home() / ".cmd_assist" / "config.yaml"
        )

    def load_yaml_config(self, path: Path) -> Dict[str, Any]:
        """Load YAML configuration from the specified path using FileUtils."""
        try:
            data = FileUtils.load_yaml(path)
            if not isinstance(data, dict):
                logger.error("YAML configuration file does not contain a dictionary")
                raise ValueError(
                    "YAML configuration file does not contain a dictionary"
                )
            return data
        except FileNotFoundError:
            logger.error("YAML configuration file not found: %s", path)
            raise
        except IOError as e:
            logger.error("IO error while loading YAML file: %s", e)
            raise
        except YAMLError as e:
            logger.error("YAML error while loading YAML file: %s", e)
            raise

    def filter_valid_fields(
        self, settings_dict: Dict[str, Any], model: AppSettings
    ) -> Dict[str, Any]:
        """Filter out invalid fields based on the model's annotations."""
        valid_fields = set(model.__annotations__.keys())
        return {
            key: value for key, value in settings_dict.items() if key in valid_fields
        }

    def get_settings(self) -> AppSettings:
        """Retrieve settings by loading from the configuration path."""
        settings_dict: Dict[str, Any] = {}

        # Load from primary configuration file if it exists
        if self.settings_path.exists():
            try:
                yaml_config = self.load_yaml_config(self.settings_path)
                logger.debug("Loaded settings from %s", self.settings_path)
                settings_dict.update(yaml_config)
            except (ValueError, IOError, YAMLError) as e:
                logger.warning(
                    "Could not load settings from %s: %s", self.settings_path, e
                )

        # Override with environment variables if they exist
        env_config = {
            key: value for key, value in os.environ.items() if key.startswith("CMD_")
        }
        settings_dict.update(env_config)

        app_settings = AppSettings(**settings_dict)
        return app_settings

    def save_persisted_settings(self, settings: AppSettings) -> None:
        """Save the specified configuration to a persistent settings file."""
        if not self.settings_path:
            raise ValueError("Settings path is not defined.")

        # Ensure parent directory exists
        settings_dir = self.settings_path.parent
        settings_dir.mkdir(parents=True, exist_ok=True)

        try:
            settings_data = {
                "commands_file": str(settings.commands_file),
                "backup_provider": settings.backup_provider or DEFAULT_BACKUP_PROVIDER,
                "object_name": settings.object_name or DEFAULT_OBJECT_NAME,
                "backup_providers": settings.backup_providers
                or {
                    "local": {
                        "directory": DEFAULT_DIRECTORY,
                        "directory_name": DEFAULT_DIRECTORY_NAME,
                    }
                },
                "bundles": settings.bundles or DEFAULT_BUNDLES,
            }
            FileUtils.save_yaml(self.settings_path, settings_data)
            logger.info("Configuration saved to %s", self.settings_path)
        except IOError as e:
            logger.error("IO error while saving configuration: %s", e)
            raise
        except YAMLError as e:
            logger.error("YAML error while saving configuration: %s", e)
            raise

    def export_config(self, output_path: Path) -> None:
        """Export the current configuration to a specified file."""
        try:
            settings = self.get_settings()
            settings_data = {
                "commands_file": str(settings.commands_file),
                "backup_provider": settings.backup_provider,
                "object_name": settings.object_name,
                "backup_providers": settings.backup_providers,
                "bundles": settings.bundles,
            }
            FileUtils.save_yaml(output_path, settings_data)
            logger.info("Configuration exported to %s", output_path)
        except IOError as e:
            logger.error("IO error while exporting configuration: %s", e)
            raise
        except YAMLError as e:
            logger.error("YAML error while exporting configuration: %s", e)
            raise
        except Exception as e:
            logger.error("Failed to export configuration: %s", e)
            raise
