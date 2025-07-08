# ☁️ Real-time Air Quality Monitoring Automation Project (공공데이터 기반 실시간 대기오염 모니터링 자동화)

### 분석 카테고리: 데이터 자동화 및 데이터 시각화
> **분석 기간** &nbsp;|&nbsp;  2025.07.03 ~ 2025.07.08  
> **분석 유형** &nbsp;|&nbsp;  개인 프로젝트  
> **분석 기법** &nbsp;|&nbsp;  API 데이터 수집 자동화, ETL 파이프라인 구축, 실시간 데이터 적재 및 대시보드 시각화  
> **분석 기술** &nbsp;|&nbsp;  ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white) ![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=flat-square&logo=GoogleCloud&logoColor=white) ![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=ApacheAirflow&logoColor=white) ![LookerStudio](https://img.shields.io/badge/LookerStudio-4285F4?style=flat-square&logo=Looker&logoColor=white)  

---

## 0. 프로젝트 구성 안내

### 📂 디렉토리 구조

```plaintext
📁 air_quality_pipeline/
 ┣ 📁 dags/                     Airflow DAG 코드
 ┣ 📁 data/                     API 응답 데이터
 ┣ 📁 notebooks/                데이터 전처리 노트북
 ┣ 📁 images/                   시각화 결과
 ┣ 📁 reports/                  프로젝트 보고서
 ┣ 📄 README.md                 프로젝트 설명 문서
 ┗ 📄 codebook.xlsx             데이터 정의서 (Code Book)
```

---

## 1. 프로젝트 개요

### 📌 세 줄 요약
- 공공데이터포털 API를 활용한 실시간 대기오염 데이터 수집 및 자동화 파이프라인 구축
- Airflow 기반 ETL → BigQuery 적재 → Looker Studio 대시보드 연계
- 운영팀의 **수동 데이터 수집 업무 100% 제거, 실시간 모니터링 시스템 구현**

---

## 2. 문제 정의 및 접근 방식

### 🔎 Situation
- 운영팀은 시도별 대기오염 정보를 실시간으로 모니터링하고 분석하는 것이 주 담당 업무
- 기존 프로세스는 대기오염 데이터를 매일 공공데이터포털에서 수동 다운로드 → 엑셀 업로드 → 대시보드 업데이트 방식
- 수동 프로세스 제거 및 실시간 변화 감지로 운영 대응시간 단축 필요

### 💡 Task
- API 호출 → 데이터 전처리 → BigQuery 적재까지 자동화된 데이터 파이프라인 구축
- Looker Studio를 통해 실시간 데이터 시각화 제공

### 🏃 Action
- **Python**: API 호출, XML 파싱
- **Airflow**: ETL 자동화 및 스케줄링
- **GCP (BigQuery + GCS)**: 데이터 적재 및 쿼리 처리
- **Looker Studio**: 실시간 시각화 대시보드

![Architecture Diagram](images/architecture.png)

### 🚀 Result
✅ **운영팀 업무 효율화**  
→ 공공데이터포털 수동 다운로드→실시간 대시보드 전환  

✅ **실시간 대시보드 구축**  
- KPI 카드, 시도별 오염도 지도, 시계열 추이 시각화
- **로드 시간: 초기 5초 → 최적화 후 1.2초**

![Dashboard Preview](images/dashboard.png)

---

## 3. 프로젝트 진행

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

### 3-4) 발표 자료 및 보고서
- 📚 [발표 자료 PDF](reports/air_quality_presentation.pdf)
- 📄 [프로젝트 요약 PDF](reports/air_quality_summary.pdf)

---

## 4. 프로젝트 회고

### ✏️ Learned Lessons
- API 인코딩/타임아웃 이슈 → 재시도 로직 추가
- Airflow v3 Composer 외부 API 호출 오류 → 서비스 계정 재설정
- BigQuery View → Materialized View로 교체 고려 (퍼포먼스 향상)
