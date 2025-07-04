
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import os

# DAG 기본 설정
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 4),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'air_quality_pipeline_v2',
    default_args=default_args,
    description='Fetch air quality data and upload to BigQuery',
    schedule_interval='@hourly',
    catchup=False,
)

# API 호출 및 CSV 저장 함수
def fetch_air_quality_data():
    api_key = "9Ds02ZptFyRbU7aeLMcyV9KDjW4/YM2TGt1Yo9mgu76ZPCV8wTkJl8poRvjwPX4gvrCDkTqS1GdrsiqLLrXMog=="
    url = f"http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={api_key}&returnType=json&numOfRows=100&pageNo=1&sidoName=서울&ver=1.0"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    rows = []
    for item in data['response']['body']['items']:
        rows.append({
            'stationName': item.get('stationName'),
            'dataTime': item.get('dataTime'),
            'pm10Value': item.get('pm10Value'),
            'pm25Value': item.get('pm25Value')
        })

    df = pd.DataFrame(rows)
    local_path = '/home/airflow/gcs/data/air_quality.csv'
    df.to_csv(local_path, index=False)

# Task 1: API 호출 및 CSV 생성
t1 = PythonOperator(
    task_id='fetch_air_quality_data',
    python_callable=fetch_air_quality_data,
    dag=dag,
)

# Task 2: GCS 업로드
t2 = LocalFilesystemToGCSOperator(
    task_id='upload_to_gcs',
    src='/home/airflow/gcs/data/air_quality.csv',
    dst='data/air_quality.csv',
    bucket='us-central1-airflow-final-476efa43-bucket',
    dag=dag,
)

# Task 3: BigQuery 적재
t3 = GCSToBigQueryOperator(
    task_id='gcs_to_bigquery',
    bucket='us-central1-airflow-final-476efa43-bucket',
    source_objects=['data/air_quality.csv'],
    destination_project_dataset_table='my-first-project.air_quality_dataset.air_quality_table',
    schema_fields=[
        {'name': 'stationName', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'dataTime', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'pm10Value', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'pm25Value', 'type': 'STRING', 'mode': 'NULLABLE'},
    ],
    write_disposition='WRITE_TRUNCATE',
    source_format='CSV',
    skip_leading_rows=1,
    dag=dag,
)

# Task 의존성 설정
t1 >> t2 >> t3
