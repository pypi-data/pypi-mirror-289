import logging
from typing import Optional

import boto3
from botocore.exceptions import ClientError

from cmd_assist.backup_handlers.exceptions import (AWSBucketCreationException,
                                                   AWSBucketDeletionException)
from cmd_assist.backup_service import BackupService
from cmd_assist.configuration.models import AWSConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class AWSManager(BackupService):
    """AWSManager class for managing AWS S3 buckets."""

    def __init__(self, config: AWSConfig, object_name: str):
        """Initialize the AWSManager service with AWSConfig and object name."""
        self.config = config
        self.object_name = object_name
        self.client = boto3.client("s3", region_name=self.config.region)

        logger.info(
            "Initialized AWSManager for region: %s, bucket: %s",
            self.config.region,
            self.config.bucket_name,
        )

    def _delete_objects(self, bucket_name: str, objects: list):
        """Delete a batch of objects from the specified bucket."""
        if objects:
            try:
                response = self.client.delete_objects(
                    Bucket=bucket_name, Delete={"Objects": objects}
                )
                logger.info("Deleted objects from bucket %s: %s", bucket_name, response)
                return response
            except ClientError as e:
                logger.error(
                    "Error deleting objects from bucket %s: %s", bucket_name, e
                )
                raise

    def _empty_bucket(self, bucket_name: str):
        """Empty all objects from the specified S3 bucket."""
        try:
            logger.info("Starting to empty bucket: %s", bucket_name)
            paginator = self.client.get_paginator("list_object_versions")
            delete_objects = []
            delete_markers = []

            for page in paginator.paginate(Bucket=bucket_name):
                versions = page.get("Versions", [])
                delete_markers_list = page.get("DeleteMarkers", [])

                for version in versions:
                    delete_objects.append(
                        {"Key": version["Key"], "VersionId": version["VersionId"]}
                    )

                for marker in delete_markers_list:
                    delete_markers.append(
                        {"Key": marker["Key"], "VersionId": marker["VersionId"]}
                    )

                if delete_objects:
                    self._delete_objects(bucket_name, delete_objects)
                    delete_objects = []

                if delete_markers:
                    self._delete_objects(bucket_name, delete_markers)
                    delete_markers = []

            response = self.client.list_objects_v2(Bucket=bucket_name)
            if (
                "Contents" in response
                or "Versions" in response
                or "DeleteMarkers" in response
            ):
                logger.warning("Bucket still contains objects after deletion attempts.")
            else:
                logger.info("Bucket is empty after deletion.")

        except ClientError as e:
            logger.error("Error emptying bucket %s: %s", bucket_name, e)
            raise

    def destroy_backup(self, resource_name: str) -> str:
        """Destroy a backup by deleting an S3 bucket after removing all its contents."""
        try:
            logger.info("Starting backup destruction for resource: %s", resource_name)
            self._empty_bucket(resource_name)
            self.client.delete_bucket(Bucket=resource_name)
            logger.info("Bucket %s deleted successfully.", resource_name)
            return "Backup destroyed successfully."
        except ClientError as e:
            logger.error("AWS client error during backup destruction: %s", e)
            raise AWSBucketDeletionException("AWS client error occurred: %s" % e) from e
        except Exception as e:
            logger.error("Unexpected error during backup destruction: %s", e)
            raise AWSBucketDeletionException(
                "Unexpected error during backup destruction: %s" % e
            ) from e

    def create_backup(self, resource_name: str) -> str:
        """Create a backup by creating a bucket."""
        return self.create_bucket(resource_name)

    def backup_exists(self, resource_name: str) -> bool:
        """Check if the backup bucket exists."""
        return self.bucket_exists(resource_name)

    def backup(self, file_path: str, resource_name: str, key: str) -> str:
        """Upload a file to the specified bucket (backup)."""
        try:
            self.upload_file(file_path, resource_name, key)
            logger.info("File %s uploaded to %s/%s.", file_path, resource_name, key)
            return f"File {file_path} uploaded to {resource_name}/{key}."
        except ClientError as e:
            logger.error(
                "Error uploading file %s to %s/%s: %s", file_path, resource_name, key, e
            )
            return f"Error uploading file: {e}"

    def restore(self, resource_name: str, key: str, local_path: str) -> str:
        """Download a file from the specified bucket (backup)."""
        try:
            self.download_file(resource_name, key, local_path)
            logger.info(
                "File %s downloaded from %s to %s.", key, resource_name, local_path
            )
            return f"File {key} downloaded from {resource_name} to {local_path}."
        except ClientError as e:
            logger.error("Error downloading file %s from %s: %s", key, resource_name, e)
            return f"Error downloading file: {e}"

    def create_bucket(self, bucket_name: str, acl: Optional[str] = None) -> str:
        """Create an S3 bucket."""
        acl = acl or self.config.bucket_acl
        try:
            if self.bucket_exists(bucket_name):
                logger.info("Bucket %s already exists.", bucket_name)
                return f"Bucket {bucket_name} already exists."

            create_bucket_config = {}
            if self.config.region != "us-east-1":
                create_bucket_config = {
                    "CreateBucketConfiguration": {
                        "LocationConstraint": self.config.region
                    }
                }

            self.client.create_bucket(
                Bucket=bucket_name, ACL=acl, **create_bucket_config
            )
            logger.info("Bucket %s created successfully.", bucket_name)
            return f"Bucket {bucket_name} created."
        except ClientError as e:
            logger.error("Error creating bucket %s: %s", bucket_name, e)
            raise AWSBucketCreationException(f"Error creating bucket: {e}") from e
        except Exception as e:
            logger.error("Unexpected error creating bucket %s: %s", bucket_name, e)
            raise AWSBucketCreationException(
                f"Unexpected error creating bucket: {e}"
            ) from e

    def delete_bucket(self, bucket_name: str) -> str:
        """Delete an S3 bucket."""

        try:
            if not self.bucket_exists(bucket_name):
                logger.info("Bucket %s does not exist.", bucket_name)
                return "Bucket %s does not exist." % bucket_name
            self.client.delete_bucket(Bucket=bucket_name)
            logger.info("Bucket %s deleted successfully.", bucket_name)
            return "Bucket %s deleted." % bucket_name
        except ClientError as e:
            logger.error("Error deleting bucket %s: %s", bucket_name, e)
            raise AWSBucketDeletionException("Error deleting bucket: %s" % e) from e
        except Exception as e:
            logger.error("Unexpected error deleting bucket %s: %s", bucket_name, e)
            raise AWSBucketDeletionException(
                "Unexpected error deleting bucket: %s" % e
            ) from e

    def bucket_exists(self, bucket_name: str) -> bool:
        """Check if an S3 bucket exists."""
        try:
            self.client.head_bucket(Bucket=bucket_name)
            logger.info("Bucket %s exists.", bucket_name)
            return True
        except ClientError:
            logger.info("Bucket %s does not exist.", bucket_name)
            return False

    def upload_file(self, file_path: str, bucket_name: str, s3_key: str) -> str:
        """Upload a file to an S3 bucket."""
        try:
            self.client.upload_file(file_path, bucket_name, s3_key)
            logger.info("File %s uploaded to %s/%s.", file_path, bucket_name, s3_key)
            return "File %s uploaded to %s/%s." % (file_path, bucket_name, s3_key)
        except ClientError as e:
            logger.error(
                "Error uploading file %s to %s/%s: %s",
                file_path,
                bucket_name,
                s3_key,
                e,
            )
            return "Error uploading file: %s" % e

    def download_file(self, bucket_name: str, s3_key: str, local_path: str) -> str:
        """Download a file from an S3 bucket."""
        try:
            self.client.download_file(bucket_name, s3_key, local_path)
            logger.info(
                "File %s downloaded from %s to %s.", s3_key, bucket_name, local_path
            )
            return "File %s downloaded from %s to %s." % (
                s3_key,
                bucket_name,
                local_path,
            )
        except ClientError as e:
            logger.error(
                "Error downloading file %s from %s: %s", s3_key, bucket_name, e
            )
            return "Error downloading file: %s" % e
