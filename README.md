# 🌱 공공 데이터 기반 '대기오염 실시간 분석 자동화' 프로젝트

### 분석 카테고리: 데이터 시각화
> **분석 기간** &nbsp;|&nbsp;  2025.07.03 ~ 2025.07.08  
> **분석 유형** &nbsp;|&nbsp;  개인 프로젝트  
> **주요 기법** &nbsp;|&nbsp;  API 데이터 수집 자동화, ETL 파이프라인 구축, 실시간 데이터 적재 및 대시보드 시각화  
> **활용 기술** &nbsp;|&nbsp;  ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white) ![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=flat-square&logo=GoogleCloud&logoColor=white) ![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=ApacheAirflow&logoColor=white) ![LookerStudio](https://img.shields.io/badge/LookerStudio-4285F4?style=flat-square&logo=Looker&logoColor=white)  

---

## 0. 프로젝트 구성 안내

### 📂 디렉토리 구조

```plaintext
📁 air_quality_pipeline/
 ┣ 📁 dags/                     Airflow DAG 코드
 ┃ ┣ 📄 air_quality_pipeline.py   대기오염 데이터 수집 및 적재 DAG
 ┃ ┣ 📄 station_mapping_dag.py    측정소 매핑 데이터 적재 DAG
 ┣ 📁 data/                     API 응답 데이터
 ┣ 📁 notebooks/                데이터 전처리 노트북
 ┣ 📁 images/                   시각화 이미지
 ┣ 📁 reports/                  프로젝트 발표 자료 및 요약 보고서
 ┣ 📄 README.md                 프로젝트 설명 문서
 ┗ 📄 codebook.xlsx             데이터 정의서 (Code Book)
```

---

## 1. 프로젝트 개요

### 📌 세 줄 요약
- 공공데이터포털의 환경공단 API를 활용해 시도별 실시간 대기오염 데이터를 수집하고 Google Cloud(BigQuery)에 적재
- Airflow 기반 ETL 파이프라인으로 자동화 및 스케줄링 처리
- BigQuery-View + Looker Studio를 연계해 실시간 대기오염 모니터링 대시보드 구축

---

## 문제 정의 및 접근 방식

### 🔎 Situation
- 데이터 분석팀은 시도별 대기오염 정보를 실시간으로 모니터링하고 분석할 필요가 있음
- 기존 방식은 공공데이터포털에서 주기적으로 데이터를 수동 다운로드 → 비효율적이고 사람이 개입해야 함

### 💡 Task
- API 호출 → 데이터 전처리 → BigQuery 적재까지 자동화된 데이터 파이프라인 구축
- Looker Studio를 통해 실시간 데이터 시각화 제공

### 🏃 Action
- 공공데이터포털 API 호출 및 XML 데이터 파싱
- pandas DataFrame 전처리 → CSV 저장
- Airflow DAG 구성 → GCS 업로드 → BigQuery 적재
- Looker Studio 연결 → 대시보드 설계 (KPI 카드, 지도, 시계열 그래프)

### 🚀 Result
- 실시간 데이터 적재 자동화 및 운영팀 활용 가능
- Looker Studio 실시간 대시보드 구축으로 데이터 활용성 극대화

---

## 프로젝트 진행

### 3-1) API 데이터 수집 및 전처리
- 공공데이터포털 API 승인 및 인증키 발급
- XML 파싱 → pandas DataFrame 처리 → CSV 저장

📄 *API 호출 및 CSV 저장 예제 코드*
```python
import requests
import pandas as pd

url = "https://apis.data.go.kr/B552584/..."
response = requests.get(url)
df = pd.DataFrame(response.json()['response']['body']['items'])
df.to_csv('data/air_quality.csv', index=False)
```

---

### 3-2) ETL 파이프라인 구축 및 자동화
- Airflow **PythonOperator** 및 **GCSToBigQueryOperator** 활용
- GCS → BigQuery 데이터 적재 및 테이블 관리
- **DAG 스케줄링**: 1시간마다 데이터 수집 자동화

📄 삽입 이미지: `images/airflow_dag_schedule.png`

---

### 3-3) Looker Studio 실시간 대시보드 설계
- BigQuery View를 **KPI**, **시도별 필터용**으로 분리
- Looker Studio에서 **실시간 데이터 연결 및 시각화**
- **주요 영역**: KPI 카드, 시도별 오염도 지도, 시간대별 변화 추이

🔗 **[실시간 대기오염 모니터링 대시보드 바로가기](#)**

📄 삽입 이미지: `images/looker_dashboard_layout.png`

---

### 📚 발표 자료 및 보고서
- 📄 [발표 자료 PDF](reports/air_quality_presentation.pdf)
- 📄 [프로젝트 요약 PDF](reports/air_quality_summary.pdf)

---

## 4. 프로젝트 회고

### ✏️ Learned Lessons

- 4-1) API부터 실시간 분석까지 End-to-End 파이프라인 설계
 - 공공데이터포털 환경공단 API를 활용해 대기오염 데이터를 수집하고, Google Cloud Platform(BigQuery)에 적재하여 실시간 대시보드를 구축했습니다.
 - 처음에는 API 호출 시 인코딩 문제와 요청 파라미터 오류로 반복적인 타임아웃이 발생했지만, API 스펙 재검토와 XML 파싱 적용으로 해결했습니다.

---

- 4-2) Airflow DAG 작성과 클라우드 자동화 트러블슈팅
 - Airflow의 **PythonOperator** 및 **GCSToBigQueryOperator**를 활용하여 GCS → BigQuery로 데이터를 자동 적재하는 파이프라인을 설계했습니다.
 - Composer(GCP Airflow) v3 환경에서는 외부 API 호출 권한, DAG 동기화 지연, 버전 차이에 따른 설정 문제를 겪었고, 공개 IP 설정 및 서비스 계정 권한 재구성으로 문제를 해결했습니다.
 - 이번 경험으로 **로컬 환경에서 DAG 테스트 후 클라우드 배포**하는 것이 효율적이라는 점을 깨달았습니다.

---

- 4-3) 실시간 대시보드를 통한 데이터 활용성 극대화
 - BigQuery View와 Looker Studio를 연계해 운영팀이 실시간으로 대기오염 데이터를 모니터링할 수 있는 대시보드를 제작했습니다.
 - KPI 카드, 시도별 오염도 지도, 시간대별 변화 추이 등 직관적인 시각화를 구현했습니다.
 - 다만 초기에는 View 쿼리 최적화 부족으로 대시보드 로딩 속도가 느려지는 이슈가 있었고, 이후 요약 View 설계와 필터 적용으로 개선했습니다.

---

- 4-4) 다음에는…
 - API 호출 단계부터 **Postman** 등으로 사전 테스트를 철저히 하고,
 - 데이터셋 설계 시 **GCS 버킷과 동일한 지역(location)** 을 지정하며,
 - 대시보드용 View는 **Materialized View**로 대체해 퍼포먼스를 높이는 방식도 고려할 계획입니다.
