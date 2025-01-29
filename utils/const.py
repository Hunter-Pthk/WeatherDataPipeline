import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET = parser.get('api_keys', 'api_key')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

selected_current_columns = [
"last_updated", "temp_c", "temp_f", "wind_mph", "humidity",
    "condition_text", "location_name", "location_region", "location_country"
]

selected_forecast_columns = [
"date", "day_maxtemp_c", "day_mintemp_c", "day_avgtemp_c", "day_totalprecip_mm",
    "day_avghumidity", "day_condition_text", "day_uv", "day_air_quality_aqi_data",
    "astro_sunrise", "astro_sunset", "astro_moon_phase"
]

