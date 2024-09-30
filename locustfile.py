from locust import HttpUser, between, task

class APIUser(HttpUser):
    wait_time = between(1, 5)  # Temps d'attente entre chaque tâche

    @task
    def get_users(self):
        self.client.get("/users")

    @task
    def create_user(self):
        self.client.post("/users", json={"name": "Performance Test User"})