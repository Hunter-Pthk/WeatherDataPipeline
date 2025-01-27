import pandas as pd
import requests
from utils.const import SECRET

url = f'http://api.weatherapi.com/v1/forecast.json?key={SECRET}&q=Toronto&days=14&aqi=yes&alerts=yes&hour=no'
response = requests.get(url)

data = response.json()

current_data = data["current"]
location_data = data["location"]

current_df = pd.json_normalize(
    current_data,
    sep="_",
)

current_df["location_name"] = location_data["name"]
current_df["location_region"] = location_data["region"]
current_df["location_country"] = location_data["country"]
current_df.to_csv("current_weather.csv", index=False)
