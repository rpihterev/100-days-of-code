import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
load_dotenv()
SHEETY_ENDPOINT = "https://api.sheety.co/e2354dc61bedb3f1ba793f71b113e3c0/flightfind/sheet1"

class DataManager:
    def __init__(self):
        self.data = {}
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)

    def get_data(self):
        self.response = requests.get(url=SHEETY_ENDPOINT,auth=self._authorization)
        self.data = self.response.text
        return self.data
