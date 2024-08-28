import logging
import requests  # Import the requests library

from executor.source_processors.processor import Processor

logger = logging.getLogger(__name__)


class ZendutyApiProcessor(Processor):
    def __init__(self, api_key):
        self.__api_key = api_key
        self.base_url = "https://www.zenduty.com/api"  # Base URL for the API

    def create_note(self, incident_number: int, content):
        try:
            # Prepare the request payload and headers
            content_payload = {
                "note": str(content)
            }
            url = f"{self.base_url}/incidents/{incident_number}/note/"
            headers = {
                'Authorization': f'Token {self.__api_key}', 
                'Content-Type': 'application/json'
            }

            # Make the POST request
            response = requests.post(url, json=content_payload, headers=headers)

            # Check if the request was successful
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

            logger.info(f"Note created successfully for incident {incident_number}")
            return response.json()  # Assuming the response is in JSON format

        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except Exception as e:
            logger.error(f"Error creating note for incident {incident_number}: {e}")

        return None