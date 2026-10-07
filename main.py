from data_manager import DataManager
import requests_cache
from datetime import datetime, timedelta
from flight_search import FlightSearch
from pprint import pprint
#Setting up Cache
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

#Talking to Sheety

data_manager = DataManager()
sheet_data = data_manager.get_data()

#Setting dates

tomorrow = tomorrow = datetime.today() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(days=180)

#Doing a flight search
search = FlightSearch()
flights = search.check_flights(
    origin_city_code = "LAX",
    destination_city_code = "AUS",
    from_time = tomorrow,
    to_time = six_months_from_today
)
print(flights)



