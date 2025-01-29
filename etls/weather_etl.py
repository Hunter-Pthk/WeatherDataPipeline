import pandas as pd
import json
import requests

from utils.const import SECRET, selected_current_columns, selected_forecast_columns


# Setting up connection to the api
def connect_weather():
    url = f'http://api.weatherapi.com/v1/forecast.json?key={SECRET}&q=Toronto&days=14&aqi=yes&alerts=yes&hour=no'
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully connected to the api...")
    else:
        print("Failed to connect")
    data = response.json()
    return data


# Extract data from current and location
def extract_current_data(data: json):
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

    return current_df


# Extracting forecast data
def extract_forecast_data(data: json):
    forecast_data = data["forecast"]["forecastday"]

    # Normalize the data into dataframe
    forecast_df = pd.json_normalize(
        forecast_data,
        sep="_"
    )
    # Loading forecast dataframe to csv file
    forecast_df.to_csv("forecast_weather.csv", index=False)
    return forecast_df


# Transformation of current weather data
def transform_current_data(current_df: pd.DataFrame):
    current_updated_df = current_df[selected_current_columns]
    return current_updated_df


# Transformation of forecast data
def transform_forecast_data(forecast_df: pd.DataFrame):
    forecast_updated_df = forecast_df[selected_forecast_columns]
    return forecast_updated_df


# Loading transformed current dataframe to csv
def load_transformed_current_to_csv(current_updated_df: pd.DataFrame, path: str):
    current_updated_df.to_csv(path, index=False)


# Loading transformed forecast dataframe to csv
def load_transformed_forecast_to_csv(forecast_updated_df: pd.DataFrame, path: str):
    forecast_updated_df.to_csv(path, index=False)
