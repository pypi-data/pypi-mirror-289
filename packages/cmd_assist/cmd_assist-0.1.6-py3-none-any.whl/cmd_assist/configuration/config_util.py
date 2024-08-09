import json
import logging
from pathlib import Path

import requests

# Configure logging
logger = logging.getLogger(__name__)


def fetch_bundle(bundle_url: str, destination: str) -> str:
    """Fetch and save a bundle from a URL."""
    destination_path = Path(destination)
    destination_path.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(bundle_url, timeout=20)
        response.raise_for_status()
        json_data = response.json()

        bundle_name = bundle_url.split("/")[-2]
        bundle_path = destination_path / f"{bundle_name}_commands.json"

        with open(bundle_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)

        return f"Commands saved to {bundle_path}"

    except requests.RequestException as e:
        logger.error("Error fetching bundle from URL '%s': %s", bundle_url, e)
        raise RuntimeError(f"Error fetching bundle from URL '{bundle_url}': {e}") from e

    except IOError as e:
        logger.error("Error writing bundle to file '%s': %s", bundle_path, e)
        raise RuntimeError(f"Error writing bundle to file '{bundle_path}': {e}") from e

    except ValueError as e:
        logger.error("Error in bundle data validation: %s", e)
        raise RuntimeError(f"Error in bundle data validation: {e}") from e

    except Exception as e:
        logger.error("An unexpected error occurred while fetching the bundle: %s", e)
        raise RuntimeError(
            f"An unexpected error occurred while fetching the bundle: {e}"
        )
