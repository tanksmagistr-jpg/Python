import requests
from config import BASE_URL, API_KEY


class YougileAPIClient:
    def __init__(self, base_url=BASE_URL, api_key=API_KEY):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def post(self, endpoint, json_data=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, headers=self.headers, json=json_data)

    def put(self, endpoint, json_data=None):
        url = f"{self.base_url}{endpoint}"
        return requests.put(url, headers=self.headers, json=json_data)

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self.headers)
