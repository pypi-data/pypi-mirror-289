import boto3
import json
import os
import tarfile
import csv
from datetime import datetime, timedelta
from kmon.kmsf_stream import kmsf_data_stream
from kmon.utility import find_latest_file


s3 = boto3.client('s3')


bucket_name = 'kmon-datalake-prod'
bi_report_bucket_name = 'bi-report-dataset'
csv_folder_prefix = 'Daily-machine-data/'
csv_file_name = 'company-count.csv'

try:
    # List objects in the specified folder
    desired_folder_prefix = 'compress/kmon_v1_raw_specif'

    file_key = find_latest_file(bucket_name, desired_folder_prefix)
    print(f"Processing latest file: {file_key}")
    response = s3.list_objects(Bucket=bucket_name, Prefix=desired_folder_prefix)
    # Check if the CSV file exists in the destination bucket
    response = s3.list_objects(Bucket=bi_report_bucket_name, Prefix=csv_folder_prefix + csv_file_name)
    csv_objects = response.get('Contents', [])

    if csv_objects:
        existing_csv_file = '/tmp/company-count.csv'
        s3.download_file(bi_report_bucket_name, csv_folder_prefix + csv_file_name, existing_csv_file)

        existing_data = []
        with open(existing_csv_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                existing_data.append(row)
    else:
        existing_data = [['Date', 'Source', 'Count', 'Company ID', 'Key ID']]

    data_map = {}
    for json_data in kmsf_data_stream(bucket_name,
                                     file_key):
        # Extract relevant data
        changed_at = json_data.get('changedAt', '')
        if isinstance(changed_at, int):
            changed_at = datetime.utcfromtimestamp(changed_at / 1000.0)
            changed_at_date = changed_at.strftime('%Y-%m-%d')
        elif isinstance(changed_at, str):
            changed_at = datetime.strptime(changed_at, '%Y-%m-%dT%H:%M:%S.%fZ')
            changed_at_date = changed_at.strftime('%Y-%m-%d')
        else:
            changed_at_date = ''

        company_id = json_data.get('companyId', '')
        key_id = json_data.get('keyId', '')
        source = json_data.get('source', '')

        # Count occurrences of each source per day
        data_map.setdefault(changed_at_date, {}).setdefault(source, {'source_count': 0, 'company_id': company_id,
                                                                          'key_id': key_id})
        data_map[changed_at_date][source]['source_count'] += 1

    # Append the new data to the existing data
    for date, sources in data_map.items():
        for source, data in sources.items():
            new_row = [date, source, data['source_count'], data['company_id'], data['key_id']]
            existing_data.append(new_row)
    #
    # # Sort the data based on the "Date" column in ascending order
    #existing_data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))

    updated_csv_file = '/tmp/updated_' + csv_file_name
    with open(updated_csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(existing_data)

    # Upload the updated CSV file to S3
    s3.upload_file(updated_csv_file, bi_report_bucket_name, csv_folder_prefix + csv_file_name)
    print("Updated CSV file uploaded to S3.")

    os.remove(existing_csv_file)
    os.remove(updated_csv_file)

except Exception as e:
    print(f"An error occurred in the Lambda: {str(e)}")
    raise e
