# pylint: skip-file
import logging
import os
from typing import Optional

import openai
from openai.error import (
    APIConnectionError,
    AuthenticationError,
    InvalidRequestError,
    OpenAIError,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class QueryHandler:
    """Query handler for OpenAI query requests."""

    def __init__(self, model="gpt-4"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        if self.api_key:
            openai.api_key = self.api_key
        else:
            raise RuntimeError(
                "OpenAI API key not set. Please set the API key to use this feature."
            )

    def get_openai_response(self, prompt: str) -> Optional[str]:
        """Fetch a response from OpenAI."""
        if not self.api_key:
            raise RuntimeError(
                "OpenAI API key not set. Please set the API key to use this feature."
            )

        try:
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
            )
            response: str = completion.choices[0].message["content"].strip()
            # If response is an empty string, handle it as a potential error
            if not response:
                raise RuntimeError("Received an empty response from OpenAI.")
            return response
        except AuthenticationError as exc:
            raise RuntimeError(
                "Authentication failed. Please check your OpenAI API key."
            ) from exc
        except APIConnectionError as exc:
            raise RuntimeError(
                "Failed to connect to OpenAI API. Check your network connection."
            ) from exc
        except InvalidRequestError as e:
            raise RuntimeError(f"Invalid request: {e}") from e
        except OpenAIError as e:
            raise RuntimeError(f"OpenAI API error: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}") from e

    def validate_query(self, category: str, subcategory: str, description: str) -> str:
        """Validate the query and check if it makes sense."""
        prompt = (
            "Given the category '%s', subcategory '%s', and description '%s', "
            "if the description makes sense, provide a command enclosed between the following prefixes: "
            "START_COMMAND and END_COMMAND. "
            "For example:\n\nSTART_COMMAND\n<your command here>\nEND_COMMAND\n\n"
            "If the description does not make sense, return 'Invalid query.'"
        ) % (category, subcategory, description)
        response = self.get_openai_response(prompt)
        # Ensure that the response is not None and return a valid string
        if response is None or not response:
            return "Invalid query"
        return response

    def process_query(
        self, category: str, subcategory: str, description: str
    ) -> Optional[str]:
        """Process the query and return the command or error."""
        try:
            validation_result = self.validate_query(category, subcategory, description)
            if validation_result.lower() == "invalid query":
                return None
            return validation_result
        except RuntimeError as e:
            logger.error("error occurred processing query %s %s", description, e)
            raise e
