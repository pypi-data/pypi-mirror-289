from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AWSConfig(BaseModel):
    """AWS configuration for the backup provider."""

    region: str = Field(default="us-east-1", description="AWS region")
    bucket_name: str = Field(default="cmd-assist-bucket", description="S3 bucket name")
    bucket_acl: str = Field(default="private", description="S3 bucket ACL")


class LocalConfig(BaseModel):
    """Local configuration for the backup provider."""

    directory: str = Field(
        default="~/.cmd_assist", description="Local backup directory"
    )
    directory_name: str = Field(
        default="backups", description="Name of the directory for backups"
    )


class AppSettings(BaseModel):
    """Application settings for the CLI."""

    commands_file: Path = Field(
        default=Path("commands.json"), description="Path to the commands file"
    )
    backup_provider: Optional[str] = Field(
        default="local", description="Backup provider (e.g., aws, local)"
    )
    object_name: str = Field(
        default="commands.json", description="Name of the resource to backup"
    )
    backup_providers: Optional[Dict[str, Dict[str, Any]]] = None  # More precise typing
    bundles: Optional[List[Dict[str, str]]] = Field(
        default_factory=list, description="List of config gists with names and URLs"
    )

    @property
    def aws(self) -> Optional[AWSConfig]:
        """Get the AWS configuration if the backup provider is AWS."""
        if self.backup_provider == "aws" and self.backup_providers:
            aws_config = self.backup_providers.get("aws", {})
            return AWSConfig(**aws_config)
        return None

    @property
    def local(self) -> Optional[LocalConfig]:
        """Get the local configuration if the backup provider is local."""
        if self.backup_provider == "local" and self.backup_providers:
            local_config = self.backup_providers.get("local", {})
            return LocalConfig(**local_config)
        return None

    def __str__(self) -> str:
        """Return a human-readable string representation of the settings."""
        settings_dict = {
            "backup_provider": self.backup_provider,
            "commands_file": str(self.commands_file),
            "object_name": self.object_name,
            "backup_providers": self.backup_providers,
            "bundles": self.bundles,
        }
        return str(settings_dict)

    def __repr__(self) -> str:
        """Return a detailed string representation of the settings."""
        return (
            "AppSettings(backup_provider=%s, "
            "commands_file=%s, "
            "object_name=%s, "
            "backup_providers=%s, "
            "bundles=%s)"
        ) % (
            self.backup_provider,
            self.commands_file,
            self.object_name,
            self.backup_providers,
            self.bundles,
        )
