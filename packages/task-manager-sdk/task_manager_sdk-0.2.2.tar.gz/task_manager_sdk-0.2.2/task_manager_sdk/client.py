import requests

class TaskManagerClient:
    def __init__(self, api_key, base_url="https://api.taskmanager.com"):
        self.api_key = api_key
        self.base_url = base_url

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data):
        response = requests.put(f"{self.base_url}/{endpoint}", json=data, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self._get_headers())
        response.raise_for_status()
        return response.status_code == 204
