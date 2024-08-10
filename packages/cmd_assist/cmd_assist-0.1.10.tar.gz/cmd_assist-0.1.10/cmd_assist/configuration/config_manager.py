import logging
from pathlib import Path
from typing import Dict, List, Optional, Union

from cmd_assist.configuration.config_util import fetch_bundle
from cmd_assist.configuration.models import AppSettings

from .config_handler import ConfigHandler

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Define type aliases
BackupProviderDetails = Dict[str, Union[str, Dict[str, str]]]
Bundles = List[Dict[str, str]]

DEFAULT_SETTINGS_PATH = Path.home() / ".cmd_assist" / "config.yaml"
DEFAULT_FALLBACK_SETTINGS_PATH = (
    Path(__file__).resolve().parent / "resources" / "config.yaml"
)


class ConfigManager:
    """Class for managing configuration settings."""

    def __init__(self, settings_path: Optional[Path] = None) -> None:
        self._settings_path = settings_path or self._resolve_settings_path()
        self._handler = ConfigHandler(settings_path=self._settings_path)
        self._settings = self.get_settings()

    def _resolve_settings_path(self) -> Path:
        """Resolve the path to the configuration file, prioritizing .cmd_assist/config.yaml."""
        if DEFAULT_SETTINGS_PATH.exists():
            return DEFAULT_SETTINGS_PATH
        return DEFAULT_FALLBACK_SETTINGS_PATH

    def get_settings(self) -> AppSettings:
        """Retrieve the current application settings."""
        return self._handler.get_settings()

    def get_config_location(self) -> Optional[Path]:
        """Get the location of the configuration."""
        return self._settings_path

    def save_settings(self) -> None:
        """Save the current configuration settings to a YAML file."""
        if not self._settings:
            raise ValueError("Settings have not been initialized.")

        if not self._handler:
            raise ValueError("ConfigHandler not initialized.")

        try:
            self._handler.save_persisted_settings(self._settings)
            logger.info("Configuration saved.")
        except (IOError, OSError) as e:
            logger.error("Failed to save configuration: %s", e)
            raise
        except ValueError as e:
            logger.error("Value error during saving configuration: %s", e)
            raise
        except Exception as e:
            logger.error("Unexpected error during saving configuration: %s", e)
            raise

    def export_settings(self, config_path: Path) -> None:
        """Export the config to a specific location."""
        if not self._handler:
            raise ValueError("ConfigHandler not initialized.")

        try:
            self._handler.export_config(output_path=config_path)
        except (IOError, OSError) as e:
            logger.error("Failed to export configuration: %s", e)
            raise
        except ValueError as e:
            logger.error("Value error during exporting configuration: %s", e)
            raise
        except Exception as e:
            logger.error("Unexpected error during exporting configuration: %s", e)
            raise

    def get_resource_name(self) -> str:
        """Retrieve the resource name based on the backup provider."""
        if not self._settings:
            raise ValueError("Settings have not been initialized.")

        if self._settings.backup_provider == "aws":
            return self._settings.aws.bucket_name if self._settings.aws else ""
        elif self._settings.backup_provider == "local":
            return self._settings.local.directory_name if self._settings.local else ""
        else:
            raise ValueError(
                f"Unsupported backup provider: {self._settings.backup_provider}"
            )

    def get_backup_provider(self) -> str:
        """Retrieve the current backup provider."""
        if not self._settings:
            return "unknown"
        return self._settings.backup_provider or "unknown"

    def get_configuration_details(self) -> AppSettings:
        """Retrieve detailed configuration information."""
        if not self._settings:
            raise ValueError("Settings have not been initialized.")
        if self._handler is None:
            raise ValueError("Handler has not been initialized.")
        config_details = self._handler.get_settings()
        if not isinstance(config_details, AppSettings):
            raise ValueError("Invalid configuration details format.")
        return config_details

    def get_bundle_url(self, bundle_name: str) -> Optional[str]:
        """Retrieve the URL for a specific bundle by name."""
        bundles = self._settings.bundles
        if not isinstance(bundles, list):
            raise ValueError("Bundles should be a list.")

        for bundle in bundles:
            if bundle.get("name") == bundle_name:
                return bundle.get("url")
        return None

    def get_bundle_names(self) -> List[str]:
        """Retrieve the names of all available bundles."""
        bundles = self._settings.bundles
        if not isinstance(bundles, list):
            raise ValueError("Bundles should be a list.")
        # Ensure 'name' is present and is a string in each bundle dictionary
        return [
            bundle["name"]
            for bundle in bundles
            if isinstance(bundle, dict) and "name" in bundle and isinstance(bundle["name"], str)
        ]

    def get_settings_path(self):
        """Retrive the settings path for the configuration"""
        return self._settings_path

    @staticmethod
    def fetch_bundle(bundle_url: str, destination: str) -> str:
        """Fetch and save a bundle from a URL using the utility function."""
        return fetch_bundle(bundle_url, destination)
