import requests
import os
from dotenv import load_dotenv
load_dotenv()
SERP_ENDPOINT = "https://serpapi.com/search.json"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["SERP_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "USD",
            "api_key": self._api_key,
        }
        response = requests.get(url=SERP_ENDPOINT, params = params)
        response.raise_for_status()
        print("from cache:", response.from_cache)
        return response.json()

