import json

import requests


class Notification:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
        }
        self.notification_url = "http://172.24.0.5:5002"

    def eloqua_register(self, content):
        return requests.post(
            url=f"{self.notification_url}/eloqua_register",
            data=json.dumps({"content": content}),
            headers=self.headers,
        )

    def sm_register(self, content):
        return requests.post(
            url=f"{self.notification_url}/sm_register",
            data=json.dumps({"content": content}),
            headers=self.headers,
        )

    def notify_reporters(self):
        return requests.get(
            url=f"{self.notification_url}/sm_reporters", headers=self.headers
        )
