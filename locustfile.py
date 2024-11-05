from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    # Wait between 1 and 3 seconds between tasks
    wait_time = between(1, 3)

    @task
    def process_data(self):
        self.client.get("/process")

    @task
    def root(self):
        # Assuming you may want to test the root endpoint as well
        self.client.get("/")

