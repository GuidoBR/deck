import json
from typing import Any, Dict
from app.services.api_client import APIClient
from app.services.message_queue import MessageQueue

class BusinessLogic:
    def __init__(self, api_client: APIClient, message_queue: MessageQueue):
        """
        Initialize the business logic with an API client and a message queue.
        
        :param api_client: A client to fetch data from external APIs
        :param message_queue: A message queue to send the processed data
        """
        self.api_client = api_client
        self.message_queue = message_queue

    def fetch_and_process_data(self) -> Dict[str, Any]:
        """
        Fetch data from an API, process it, and enqueue the result to a message queue.

        :return: Processed data
        """
        try:
            raw_data = self.api_client.fetch_data()

            processed_data = self.process_data(raw_data)

            self.message_queue.send_message(processed_data)

            return processed_data

        except Exception as e:
            print(f"Error during data processing: {e}")

    def process_data(self, data: Any) -> Dict[str, Any]:
        """
        Process the raw data fetched from the API.
        
        :param data: Raw data fetched from the API
        :return: Processed data
        """
        return {
            "transformed_data": data,
            "status": "processed"
        }

