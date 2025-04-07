from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Users wait 1-2 seconds before making a new request

    @task
    def load_test(self):
        self.client.get("learn/career-path/devops-and-cloud-computing-course-JAN-Batch/67763fb09c7eb6fec2f20ecf/dashboard/?from=/learn/&clickText=continue&page_from=my_course_page")
