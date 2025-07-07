from airflow import models
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime, timedelta
import requests
import pandas as pd

def fetch_air_quality_data():
    API_KEY = "본인이 받은 인증키"
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    params = {
        "serviceKey": API_KEY,
        "returnType": "json",
        "numOfRows": "10",
        "pageNo": "1",
        "sidoName": "서울",
        "ver": "1.0"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    items = data['response']['body']['items']
    df = pd.json_normalize(items)
    
    # 저장 경로: Airflow의 GCS data 폴더
    df.to_csv("/home/airflow/gcs/data/air_quality.csv", index=False, encoding="utf-8-sig")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 7, 7),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = models.DAG(
    "air_quality_pipeline_final",
    default_args=default_args,
    description="Fetch air quality data and load to BigQuery",
    schedule_interval="@hourly",
    catchup=False,
)

fetch_task = PythonOperator(
    task_id="fetch_air_quality_data",
    python_callable=fetch_air_quality_data,
    dag=dag,
)

load_task = GCSToBigQueryOperator(
    "본인이 받은 빅쿼리 인증키"
)

fetch_task >> load_task
