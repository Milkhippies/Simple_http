import random
from server import client
from locust import HttpUser, TaskSet, task


class WebsiteUser(HttpUser):

    num = 5

    @task(2)
    def get(self, maxID = num):
        self.client.get("/tutorials/" + str(random.randint(0, maxID)))

    @task(1)
    def post(self, maxID= num):
        postdata = {
            "id": maxID+1,
            "title": 'random post data',
            "description": 'hehe, its post'
        }
        self.client.post("/tutorials", json = postdata)

    #@task(1)
    # def put(self , maxID=None):
    #     rnd = random.randint(0, maxID)
    #     data = {
    #         "id": rnd,
    #         "title": 'random put data',
    #         "description": 'hehe, its put'
    #     }
    #     self.client.put("/tutorials/" + str(rnd), json=data)

    min_wait = 100
    max_wait = 200
