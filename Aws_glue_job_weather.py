import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1738692958578 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://pthk-weather-pipeline/raw/weather_forecast_20250204.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1738692958578")

# Script generated for node Drop Fields
DropFields_node1738700441025 = DropFields.apply(frame=AmazonS3_node1738692958578, paths=["day_air_quality_aqi_data"], transformation_ctx="DropFields_node1738700441025")

# Script generated for node Amazon S3
AmazonS3_node1738700463330 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1738700441025, connection_type="s3", format="csv", connection_options={"path": "s3://pthk-weather-pipeline/transformed/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1738700463330")

job.commit()