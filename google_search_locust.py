from locust import HttpUser, task, between

class GoogleSearchUser(HttpUser):
    host = "https://www.google.com"  # Specify the base host (Google in this case)
    wait_time = between(1, 3)  # Random wait time between requests

    @task
    def search_google(self):
        # Perform a Google search for "car"
        self.client.get("/search?q=car")

    # You can add more tasks here if needed
    # For example, clicking on search results or navigating to other pages

# Run Locust with the following command:
# locust -f google_search_locust.py
# locust runs until we either stop it or we specify duration such as this:
# locust -f google_search_locust.py --run-time 5m
# after we run code in the terminal we should use the web app on :
# http://localhost:8089  , there we can specify number of VS and see stats etc.
