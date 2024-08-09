import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import ValidationError
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

    def __init__(self, settings_path: Optional[Path] = None):
        self.settings_path = settings_path or (
            Path.home() / ".cmd_assist" / "cli_settings.yaml"
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
        """Retrieve settings by loading from the specified configuration path."""
        primary_config_path = self._get_primary_config_path() or self.settings_path

        # Start with an empty settings dictionary
        settings_dict: Dict[str, Any] = {}

        # Load from primary configuration file if it exists
        if primary_config_path and primary_config_path.exists():
            try:
                yaml_config = self.load_yaml_config(primary_config_path)
                logger.debug("Loaded settings from %s", primary_config_path)
                settings_dict.update(yaml_config)
            except (ValueError, IOError, YAMLError) as e:
                logger.warning(
                    "Could not load settings from %s: %s", primary_config_path, e
                )

        # Override with environment variables if they exist
        env_config = {
            key: value for key, value in os.environ.items() if key.startswith("CMD_")
        }
        settings_dict.update(env_config)

        # Validate and convert to AppSettings model
        config_path_loc = str(primary_config_path)
        app_settings = AppSettings(config_path=config_path_loc)
        settings_dict = self.filter_valid_fields(settings_dict, app_settings)
        settings_dict["bundles"] = settings_dict.get("bundles", [])

        # Exclude config_path from settings_dict to avoid conflict
        settings_dict.pop("config_path", None)

        try:
            return AppSettings(config_path=str(primary_config_path), **settings_dict)
        except ValidationError as e:
            logger.error("Configuration validation error: %s", e)
            raise
        except Exception as e:
            logger.error(
                "An unexpected error occurred while retrieving settings: %s", e
            )
            raise

    def save_persisted_settings(self, settings: AppSettings) -> None:
        """Save the specified configuration to a persistent settings file."""
        if not self.settings_path:
            raise ValueError("Settings path is not defined.")

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
                "config_path": (
                    str(settings.config_path) if settings.config_path else None
                ),
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
                "config_path": (
                    str(settings.config_path) if settings.config_path else None
                ),
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

    def _get_primary_config_path(self) -> Optional[Path]:
        """Determine the primary configuration path based on user settings and provided path."""
        # Load settings from the default CLI settings path
        try:
            settings = self.load_yaml_config(self.settings_path)
            config_path_str = settings.get("config_path")
            if config_path_str:
                config_path = Path(config_path_str)
                if config_path.exists():
                    return config_path
                else:
                    logger.warning(
                        "Configured config_path does not exist: %s", config_path_str
                    )
        except (ValueError, IOError, YAMLError) as e:
            logger.warning("Could not load settings or validate config_path: %s", e)

        # Fallback to the default settings path
        default_settings_path = Path.home() / ".cmd_assist" / "cli_settings.yaml"
        return default_settings_path if default_settings_path.exists() else None
