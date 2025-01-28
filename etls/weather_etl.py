import pandas as pd
import requests
from utils.const import SECRET, selected_current_columns, selected_forecast_columns

url = f'http://api.weatherapi.com/v1/forecast.json?key={SECRET}&q=Toronto&days=14&aqi=yes&alerts=yes&hour=no'
response = requests.get(url)

data = response.json()

# Extract data from current and location
current_data = data["current"]
location_data = data["location"]

# Normalize nested json to flatten the data by creating dataframe
current_df = pd.json_normalize(
    current_data,
    sep="_",
)

# Merging location data into current weather data
current_df["location_name"] = location_data["name"]
current_df["location_region"] = location_data["region"]
current_df["location_country"] = location_data["country"]

# Loading dataframe into csv file
current_df.to_csv("current_weather.csv", index=False)

# Selection of few important columns
current_updated_df = current_df[selected_current_columns]

# Loading to csv
current_updated_df.to_csv("current_updated_weather.csv", index=False)

#Extracting forecast data
forecast_data = data["forecast"]["forecastday"]

# Normalize the data into dataframe
forecast_df = pd.json_normalize(
    forecast_data,
    sep="_"
)

# Loading forecast dataframe to csv file
forecast_df.to_csv("forecast_weather.csv", index=False)

# Selection of updated columns
forecast_updated_df = forecast_df[selected_forecast_columns]
forecast_updated_df.to_csv("forecast_updated_weather.csv", index=False)



