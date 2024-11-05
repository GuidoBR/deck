from app.services.api_client import APIClient

class BusinessLogic:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def process_data(self):
        data = self.api_client.fetch_data()
        
        data["processed"] = True
        
        self.enqueue_data(data)
        return data

    def enqueue_data(self, data):
        print(f"Data enqueued: {data}") # TODO
