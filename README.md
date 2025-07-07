# 🌱 공공 데이터 기반 '대기오염 실시간 분석 자동화' 프로젝트

### 분석 카테고리:
> **분석 기간** &nbsp;|&nbsp;  2025.07.03 - 2025.07.08 <br/>
> **분석 주체** &nbsp;|&nbsp;  개인 프로젝트 <br/>
> **분석 기법** &nbsp;|&nbsp;  API 데이터 수집 자동화, ETL 파이프라인 구축, 시계열 데이터 분석, 실시간 데이터 적재 및 시각화 <br/>
> **분석 기술** &nbsp;|&nbsp;  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/BigQuery-4285F4?style=flat-square&logo=GoogleCloud&logoColor=white"/> <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=ApacheAirflow&logoColor=white"/> <img src="https://img.shields.io/badge/ETL-FF6F00?style=flat-square"/> <img src="https://img.shields.io/badge/REST%20API-005571?style=flat-square&logo=api&logoColor=white"/>  

---

## 0. 프로젝트 구성 안내

### 📂 디렉토리 구조

```plaintext
📁 air_quality_data_pipeline/
 ┣ 📁 data/                  API 응답 데이터 및 CSV 파일
 ┣ 📁 dags/                  Airflow DAG 코드
 ┣ 📁 notebooks/             데이터 수집 및 전처리 Colab 노트북
 ┣ 📁 images/                시각화 결과 (막대 그래프, 지도 등)
 ┣ 📁 reports/               분석 보고서 및 PPT 자료
 ┣ 📄 README.md              프로젝트 설명 문서
 ┣ 📄 requirements.txt       사용한 Python 패키지 목록
 ┗ 📄 codebook.xlsx          데이터 정의서 (Code Book)
```

---

## 1. 프로젝트 개요  

### 📌  세 줄 요약  
- 공공데이터포털의 에어코리아 대기오염 API를 활용해 실시간 대기오염 데이터 수집 및 Google Cloud(BigQuery)에 적재
- Airflow 기반 ETL 파이프라인 구축으로 데이터 적재 작업 자동화 
- 시간·지역별 대기오염 패턴 분석 및 시각화를 통해 대기질 변화 트렌드 도출
---

## 2. 문제 정의 및 접근 방식  

### 🔍 **Situation**  
- 데이터 분석팀에서 시도별 대기오염 정보의 실시간 모니터링과 분석이 필요
- 기존 방식은 공공데이터포털에서 주기적으로 데이터를 수동 다운로드 → 비효율적이며 사람 의존도가 높음 

### 💡 **Task**  
- API 호출 → 데이터 전처리 → BigQuery 적재까지 자동화된 데이터 파이프라인 구축
- 실시간으로 조회·분석 가능한 시스템 구축

### 🏃 **Action**  
- 공공데이터포털 API 호출 및 XML 데이터 파싱  
- pandas DataFrame 전처리 → CSV 파일 생성
- Airflow DAG 구성으로 ETL 자동화 및 스케줄링 수행  
- BigQuery에서 분석 진행

### 🚀 **Result**  
- 실시간 데이터 적재 자동화 성공 (Airflow 스케줄링)  
- BigQuery 기반 대기오염 분석으로 시간·지역별 오염 패턴 도출  
- 데이터 분석팀에서 바로 사용할 수 있는 데이터 파이프라인 제공  

---

## 3. 프로젝트 진행  

### 3-1) 📡 API 데이터 수집 및 전처리  
- Open API 승인 → XML 데이터 파싱 → pandas DataFrame 변환  
- 주요 변수: SO2, CO, O3, NO2, PM10, PM2.5 등 대기오염 지표  
- 결과 데이터 CSV 저장 및 BigQuery 적재  

![삽입 이미지](images/api_response_to_bigquery.png)  

---

### 3-2) 🛠 ETL 파이프라인 구축 및 Airflow 스케줄링  
- Airflow DAG 구성: PythonOperator로 API 호출 → 데이터 전처리 → GCS 업로드 → BigQuery 적재
- DAG 실행 주기: 매 1시간마다 데이터 수집 및 적재  

📄 삽입 이미지: `images/airflow_dag_schedule.png`  

---

### 3-3) 📈 분석 및 시각화  
- BigQuery SQL 쿼리 분석으로 지역별 오염도 트렌드 파악
- 시간대별 오염물질 농도 분포 시각화 및 지역 간 비교

📄 삽입 이미지: `images/air_quality_trend_bar_chart.png`  
📄 삽입 이미지: `images/region_air_pollution_map.png`  

---

## 4. 프로젝트 회고

### ✏️ Learned Lessons
- 공공 데이터 API → 데이터 전처리 → GCP 적재 → 실시간 분석까지 End-to-End 경험  
- Airflow DAG 구성과 스케줄링을 통해 데이터 파이프라인 자동화의 가치 체감  
- 실시간 데이터 분석을 통해 운영팀의 업무 효율성 향상 가능성 확인

### ✏️ Learned Lessons

- **API부터 실시간 분석까지 End-to-End 파이프라인 설계**  
 - 공공데이터포털 환경공단 API를 활용해 대기오염 데이터를 수집하고, Google Cloud Platform(BigQuery)에 적재하여 실시간 대시보드를 구축했습니다. 이 과정에서 API 인증키 관리, JSON/XML 데이터 파싱, 데이터셋 스키마 설계 등 실무적인 절차를 경험했습니다.  
 - 처음에는 API 호출 시 인코딩 문제와 요청 파라미터 오류로 반복적인 타임아웃이 발생했지만, API 스펙 재검토와 XML 파싱 적용으로 해결했습니다.

- **Airflow DAG 작성과 클라우드 자동화 트러블슈팅**  
 - Airflow의 PythonOperator 및 GCSToBigQueryOperator를 활용하여 GCS → BigQuery로 데이터를 자동 적재하는 파이프라인을 설계했습니다. Composer(GCP Airflow) v3 환경에서는 외부 API 호출 권한, DAG 동기화 지연, 버전 차이에 따른 설정 문제를 겪었고, 공개 IP 설정 및 서비스 계정 권한 재구성으로 문제를 해결했습니다.  
 - 이번 경험으로 로컬 환경에서 DAG 테스트 후 클라우드 배포하는 것이 효율적이라는 점을 깨달았습니다.

- **실시간 대시보드를 통한 데이터 활용성 극대화**  
 - BigQuery View와 Looker Studio를 연계해 운영팀이 실시간으로 대기오염 데이터를 모니터링할 수 있는 대시보드를 제작했습니다. KPI 카드, 시도별 오염도 지도, 시간대별 변화 추이 등 직관적인 시각화를 구현했습니다.  
 - 다만 초기에는 View 쿼리 최적화 부족으로 대시보드 로딩 속도가 느려지는 이슈가 있었고, 이후 요약 View 설계와 필터 적용으로 개선했습니다.

- **다음에는…**  
 - API 호출 단계부터 Postman 등으로 사전 테스트를 철저히 하고,  
 - 데이터셋 설계 시 GCS 버킷과 동일한 지역(location)을 지정하며,  
 - 대시보드용 View는 Materialized View로 대체해 퍼포먼스를 높이는 방식도 고려할 계획입니다.
