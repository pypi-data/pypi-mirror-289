from cmd_assist.backup_handlers.aws import AWSManager
from cmd_assist.backup_handlers.local import LocalBackup
from cmd_assist.backup_service import BackupService
from cmd_assist.configuration.models import AppSettings


class BackupFactory:
    """Factory class for creating backup services based on the provider."""

    @staticmethod
    def get_instance(settings: AppSettings) -> BackupService:
        """Return a backup service instance based on the provider."""
        # Ensure backup_provider is not None and convert to lowercase
        backup_provider = settings.backup_provider
        if backup_provider == "aws":
            if not settings.aws:
                raise ValueError("AWS settings are not specified in the configuration.")
            return AWSManager(settings.aws, settings.object_name)
        elif backup_provider == "local":
            if not settings.local:
                raise ValueError(
                    "Local settings are not specified in the configuration."
                )
            return LocalBackup(settings.local, settings.object_name)
        else:
            raise ValueError(f"Unsupported backup provider: {backup_provider}")
