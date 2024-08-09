import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')


def find_latest_file(bucket_name, base_prefix):
  # Convert start_date_str to datetime object
  start_date = datetime.today()

  while True:
    # Construct the key with the current date
    date_str = start_date.strftime('%Y-%m-%d')
    prefix = f"{base_prefix}/{date_str}"

    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, MaxKeys=1)
    contents = response.get('Contents', [])
    if len(contents) > 0:
      file_name = contents[0]['Key']
      return file_name
    # If file does not exist, decrement the date
    start_date -= timedelta(days=1)

    # Optional: Stop condition if you reach a specific date
    # You can add a condition to stop at a specific date to avoid infinite loop
    # For example, stop if you go back more than a year
    if start_date < datetime.now() - timedelta(days=365):
      print("No files found within one year.")
      return None