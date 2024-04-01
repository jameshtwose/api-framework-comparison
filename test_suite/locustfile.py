from locust import HttpUser, task
import numpy as np

class TestUser(HttpUser):
    @task
    def general_get(self):
        self.client.get("/")
        self.client.get("/complaints?limit=10")
    
    # increasing the amount of complaints by call 
    @task
    def increasing_complaints(self):
        for limit in np.arange(10, 100000, 10):
            self.client.get(f"/complaints?limit={limit}", name="/complaints?limit=[limit]")