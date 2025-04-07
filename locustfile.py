from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Users wait 1-2 seconds before making a new request

    @task
    def load_test(self):
        self.client.get("course/devops-and-cloud-computing-course-JAN-Batch/67763fb09c7eb6fec2f20ecf/lesson/67ee6fa074ee33dbc16f2ca3/?lectureType=video&milestoneId=677651c79c7eb6fec2f23d69&sectionId=678b75ae2b28919111f6b55c")
