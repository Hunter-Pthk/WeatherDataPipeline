from etls.weather_etl import connect_weather, extract_forecast_data, extract_current_data, transform_current_data, \
    transform_forecast_data, load_transformed_current_to_csv, load_transformed_forecast_to_csv
from utils.const import OUTPUT_PATH


def weather_pipeline(file_name1: str, file_name2: str):
    # Connection to api
    data = connect_weather()

    # Extraction of current and location data
    current_df = extract_current_data(data)

    # Extraction of forecast data
    forecast_df = extract_forecast_data(data)

    # Transformation of current data
    current_transformed_df = transform_current_data(current_df)

    #Transformation of forecast data
    forecast_transformed_df = transform_forecast_data(forecast_df)

    # Loading current dataframe to csv
    file_path1 = f'{OUTPUT_PATH}/{file_name1}.csv'
    load_transformed_current_to_csv(current_transformed_df, file_path1)

    # Loading forecast dataframe to csv
    file_path2 = f'{OUTPUT_PATH}/{file_name2}.csv'
    load_transformed_forecast_to_csv(forecast_transformed_df, file_path2)
    return file_path1, file_path2