import random

class APIClient:
    def fetch_data(self):
        # Simulate calling a third-party API and returning a mock response
        mock_response = {
            "id": random.randint(1, 100),
            "name": "Sample Data",
            "value": random.uniform(10.0, 100.0)
        }
        return mock_response
