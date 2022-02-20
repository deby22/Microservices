import requests


class Notification:
    def __init__(self):
        self.notification_url = "http://localhost:5002"

    def eloqua_register(self, content):
        return requests.post(f"/eloqua_register", body={"content": content})

    def sm_register(self, content):
        return requests.post(f"/sm_register", body={"content": content})

    def notify_reporters(self):
        return requests.get(f"/sm_reporters")
