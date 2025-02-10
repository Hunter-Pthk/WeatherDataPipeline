from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.const import AWS_BUCKET_NAME


def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='Weather_extraction', key='return_value')

    # Unpacking tuple into two files
    current_weather_file, forecast_weather_file = file_path

    s3 = connect_to_s3()
    create_bucket_if_not_exist(s3,AWS_BUCKET_NAME)
    upload_to_s3(s3, current_weather_file, AWS_BUCKET_NAME, current_weather_file.split('/')[-1])
    upload_to_s3(s3, forecast_weather_file, AWS_BUCKET_NAME, forecast_weather_file.split('/')[-1])

