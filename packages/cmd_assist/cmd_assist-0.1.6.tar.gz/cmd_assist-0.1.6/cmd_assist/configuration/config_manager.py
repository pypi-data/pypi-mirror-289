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
CONFIG_DETAILS = Dict[str, Union[str, BackupProviderDetails, Bundles]]

DEFAULT_SETTINGS_PATH = Path.home() / ".cmd_assist" / "cli_settings.yaml"
DEFAULT_FALLBACK_SETTINGS_PATH = (
    Path(__file__).resolve().parent / "resources" / "config.yaml"
)


class ConfigManager:
    """Singleton class for managing configuration settings."""

    _instance: Optional["ConfigManager"] = None
    _settings_path: Optional[Path] = None
    _settings: Optional[AppSettings] = None
    _handler: Optional[ConfigHandler] = None
    _initialized: bool = False

    def __new__(cls, settings_path: Optional[Path] = None) -> "ConfigManager":
        if cls._instance is None or settings_path != cls._settings_path:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(settings_path)
        return cls._instance

    def __init__(self, settings_path: Optional[Path] = None) -> None:
        # Ensure _initialize is only called once
        if self._initialized:
            return

        self._settings_path = settings_path or self._resolve_settings_path()
        self._handler = ConfigHandler(settings_path=self._settings_path)
        self._settings = self.get_settings()
        self._initialized = True

    def _initialize(self, settings_path: Optional[Path]) -> None:
        """Initialize instance attributes."""
        if self._initialized:
            return

        # No direct call to self.__init__ to avoid recursion issues
        self._settings_path = settings_path or self._resolve_settings_path()
        self._handler = ConfigHandler(settings_path=self._settings_path)
        self._settings = self.get_settings()
        self._initialized = True

    @classmethod
    def get_instance(cls, settings_path: Optional[Path] = None) -> "ConfigManager":
        """Get the singleton instance of the ConfigManager class."""
        if cls._instance is None or settings_path != cls._settings_path:
            cls._instance = cls(settings_path=settings_path)
        return cls._instance

    def _resolve_settings_path(self) -> Path:
        """Resolve the path to the configuration file, prioritizing .cmd_assist/cli_settings.yaml."""
        if DEFAULT_SETTINGS_PATH.exists():
            return DEFAULT_SETTINGS_PATH
        return DEFAULT_FALLBACK_SETTINGS_PATH

    def get_settings(self) -> AppSettings:
        """Retrieve the current application settings."""
        if not self._settings:
            if not self._handler:
                raise ValueError("ConfigHandler not initialized.")
            self._settings = self._handler.get_settings()
        return self._settings

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

    def get_configuration_details(self) -> CONFIG_DETAILS:
        """Retrieve detailed configuration information."""
        if not self._settings:
            raise ValueError("Settings have not been initialized.")

        config_details: CONFIG_DETAILS = {
            "backup_provider": self._settings.backup_provider or "",
            "commands_file": str(self._settings.commands_file),
            "object_name": self._settings.object_name,
        }

        if self._settings.backup_provider == "aws" and self._settings.backup_providers:
            aws_details = self._settings.backup_providers.get("aws", {})
            config_details["aws"] = aws_details

        if (
            self._settings.backup_provider == "local"
            and self._settings.backup_providers
        ):
            local_details = self._settings.backup_providers.get("local", {})
            config_details["local"] = local_details

        if self._settings.bundles:
            config_details["bundles"] = self._settings.bundles

        return config_details

    def get_bundle_url(self, bundle_name: str) -> Optional[str]:
        """Retrieve the URL for a specific bundle by name."""
        if not self._settings or not self._settings.bundles:
            return None

        for bundle in self._settings.bundles:
            if bundle.get("name") == bundle_name:
                return bundle.get("url")

        return None

    def get_bundle_names(self) -> List[str]:
        """Retrieve the names of all available bundles."""
        if not self._settings or not self._settings.bundles:
            return []

        return [
            name
            for bundle in self._settings.bundles
            if (name := bundle.get("name")) is not None
        ]

    @staticmethod
    def fetch_bundle(bundle_url: str, destination: str) -> str:
        """Fetch and save a bundle from a URL using the utility function."""
        return fetch_bundle(bundle_url, destination)
