from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Users wait 1-2 seconds before making a new request

    @task
    def load_test(self):
        self.client.get("/target-endpoint")  # Replace with your actual API endpoint

