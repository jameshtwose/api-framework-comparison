from locust import HttpUser, task
import numpy as np


class TestUser(HttpUser):
    @task
    def get_root(self):
        self.client.get("/")

    @task
    def get_complaints(self):
        # self.client.get("/")
        self.client.get("/complaints?limit=10")

    # increasing the amount of complaints by call
    @task
    def increasing_complaints(self):
        for limit in np.arange(10, 100000, 10):
            self.client.get(
                f"/complaints?limit={limit}", name="/complaints?limit=[limit]"
            )

    @task
    def get_prices(self):
        self.client.get("/prices?limit=10")

    @task
    def get_price(self):
        self.client.get("/prices/7968391")

    @task
    def get_complaint_price(self):
        self.client.get("/complaints/7968391/price")

    @task
    def get_complaint(self):
        self.client.get("/complaints/7968391")

    @task
    def get_complaints_by_date(self):
        self.client.get("/complaints/date_received/2023-12-09")
        
    # @task
    # def get_all_complaints_w_prices(self):
    #     self.client.get("/complaints/price/all")

    @task
    def insert_price(self):
        self.client.post("/prices?complaint_id=1&price=100")

    @task
    def delete_price(self):
        self.client.delete("/prices/1")

    @task
    def fail_request(self):
        self.client.get("/fail")