import logging
import os
from pathlib import Path
from typing import Any, Dict

import yaml

from cmd_assist.constants import DEFAULT_COMMANDS_PATH

# Default path for commands file


# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class FileUtils:
    """util for file operations"""

    @staticmethod
    def load_yaml(file_path: Path) -> Dict[str, Any]:
        file_path = Path(file_path)
        if file_path.exists():
            logger.debug(f"Loading YAML file from {file_path}")
            try:
                with open(file_path, "r") as f:
                    data = yaml.safe_load(f) or {}
                logger.debug(f"Successfully loaded YAML file from {file_path}")
                return data
            except yaml.YAMLError as e:
                logger.error(f"Error parsing YAML file from {file_path}: {e}")
                return {}
            except Exception as e:
                logger.error(
                    f"Unexpected error loading YAML file from {file_path}: {e}"
                )
                return {}
        else:
            logger.debug(f"YAML file not found at {file_path}")
            return {}

    @staticmethod
    def save_yaml(file_path: Path, data: dict) -> None:
        """Save data to a YAML file."""
        if not isinstance(data, dict):
            logger.error("Data to save must be a dictionary.")
            raise ValueError("Data must be a dictionary.")

        logger.debug(f"Saving YAML file to {file_path}")
        try:
            with file_path.open("w") as f:
                yaml.safe_dump(data, f, default_flow_style=False)
            logger.info(f"Successfully saved YAML file to {file_path}")
        except IOError as e:
            logger.error(f"IO error while saving YAML file to {file_path}: {e}")
            raise
        except yaml.YAMLError as e:
            logger.error(f"YAML error while saving YAML file to {file_path}: {e}")
            raise

    @staticmethod
    def get_default_location():
        """Get the location for the commands file, checking environment variable or falling back to default."""
        location = os.getenv("CMD_STASH_LOCATION")

        if location is None:
            location = DEFAULT_COMMANDS_PATH

        default_path = Path(location)
        if not default_path.exists():
            logger.debug(f"Default path {default_path} does not exist. Creating it.")
            try:
                default_path.parent.mkdir(parents=True, exist_ok=True)
                default_path.touch()  # Create the file if it does not exist
                logger.debug(f"Default path {default_path} created.")
            except IOError as e:
                logger.error(
                    f"IO error while creating default path {default_path}: {e}"
                )
                raise
            except Exception as e:
                logger.error(f"Error creating default path {default_path}: {e}")
                raise

        if not os.getenv("CMD_STASH_LOCATION"):
            os.environ["CMD_STASH_LOCATION"] = str(default_path)
            logger.debug(
                f"Environment variable CMD_STASH_LOCATION set to {default_path}"
            )

        return str(default_path)
