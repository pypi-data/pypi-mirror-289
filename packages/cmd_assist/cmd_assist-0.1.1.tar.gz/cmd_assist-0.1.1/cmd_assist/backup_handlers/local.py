import json
import logging
import shutil
from datetime import datetime
from pathlib import Path

from cmd_assist.backup_service import BackupService
from cmd_assist.configuration.models import LocalConfig

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class LocalBackup(BackupService):
    """Local backup service for storing files on the local filesystem."""

    def __init__(self, config: LocalConfig, object_name: str):
        """Initialize the LocalBackup service with configuration."""
        self.config = config
        self.object_name = object_name

        # Convert config directory and directory_name to Path objects if they are strings
        self.directory = (
            Path(self.config.directory)
            if isinstance(self.config.directory, str)
            else self.config.directory
        )
        self.directory_name = (
            Path(self.config.directory_name)
            if isinstance(self.config.directory_name, str)
            else self.config.directory_name
        )
        self.location = self.directory / self.directory_name

        # Ensure the backup directory exists
        self.location.mkdir(parents=True, exist_ok=True)

        logger.debug("Backup location initialized at %s", self.location)
        logger.debug("Object name for backup set to %s", self.object_name)

    def create_backup(self, resource_name: str) -> str:
        """Create a backup directory and initialize it with an empty file."""
        backup_dir = self.location / resource_name
        logger.debug("Creating backup directory at: %s", backup_dir)

        # Ensure the directory for the backup exists
        backup_dir.mkdir(parents=True, exist_ok=True)
        logger.debug("Backup directory created or already exists: at %s", backup_dir)

        # Create the object_name file inside the directory
        object_path = backup_dir / self.object_name
        logger.debug("Creating object file at %s", object_path)

        # Create an empty file or initialize it with some default content
        with object_path.open("w") as file:
            json.dump(
                {}, file
            )  # Create an empty JSON file or initialize with default content

        message = f"Backup directory for {resource_name} created at {backup_dir}, with file {self.object_name}."
        logger.info(message)
        return message

    def backup_exists(self, resource_name: str) -> bool:
        """Check if the backup directory for the resource exists."""
        backup_dir = self.location / resource_name
        exists: bool = backup_dir.exists()
        logger.debug(
            "Backup existence check for %s: %s",
            resource_name,
            "exists" if exists else "does not exist",
        )
        return exists

    def backup(self, file_path: str, resource_name: str, key: str) -> str:
        """Backup a file to the specified directory."""
        logger.debug(
            "Starting backup process for file_path: %s, resource_name: %s, key: %s",
            file_path,
            resource_name,
            key,
        )

        backup_dir = self.location / resource_name
        logger.debug("Backup directory path: %s", backup_dir)

        # Ensure the backup directory exists
        backup_dir.mkdir(parents=True, exist_ok=True)
        logger.debug("Ensured existence of backup directory: %s", backup_dir)

        # Use the object_name from settings as the base filename
        base_filename = self.object_name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_key = f"{base_filename.split('.')[0]}_{timestamp}.txt"
        destination_path = backup_dir / new_key
        logger.debug("New backup file path: %s", destination_path)

        # Copy the file to the backup directory
        shutil.copy(file_path, destination_path)
        logger.debug("Copied file from %s to %s", file_path, destination_path)

        message = f"File {file_path} backed up to {destination_path}."
        logger.info(message)
        return message

    def restore(self, resource_name: str, key: str, local_path: str) -> str:
        """Restore a file from the backup to a local path."""
        backup_dir = self.location / resource_name
        source_path = backup_dir / key

        # Ensure both paths are strings
        source_path_str = (
            str(source_path) if isinstance(source_path, Path) else source_path
        )
        local_path_str = str(local_path) if isinstance(local_path, Path) else local_path

        logger.debug("Restoring file from %s to %s", source_path_str, local_path_str)

        if not source_path.exists():
            logger.error("Source file does not exist: %s", source_path_str)
            raise FileNotFoundError(f"Source file does not exist: {source_path_str}")

        shutil.copy(source_path_str, local_path_str)
        logger.debug("Restored file to %s", local_path_str)

        message = f"File {source_path_str} restored to {local_path_str}."
        logger.info(message)
        return message

    def destroy_backup(self, resource_name: str) -> str:
        """Destroy the backup directory."""
        backup_dir = self.location / resource_name
        logger.debug("Attempting to delete backup directory: %s", backup_dir)

        if backup_dir.exists():
            shutil.rmtree(backup_dir)
            message = f"Backup directory for {resource_name} deleted."
            logger.info(message)
            return message
        else:
            message = f"Backup directory for {resource_name} does not exist."
            logger.warning(message)
            return message
