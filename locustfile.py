from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Users wait 1-2 seconds before making a new request

    @task
    def load_test(self):
        self.client.get("/course/dsa-in-python/?source=pwskills.com&position=course_dropdown&from=home_page")  # Replace with your actual API endpoint

