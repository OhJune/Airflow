# Airflow 

![image](https://github.com/OhJune/Airflow/assets/124857930/8f9387b6-5c16-48b9-9bc1-ec3e541c36d5)


### 1. 신곡 수집 자동화
  > TJ, KY 노래 데이터 수집 -> 전처리 -> postgresql DB 적재

      1-1. 하루 간격으로 수집되는 신곡 업데이트! 
      1-2. TJ와 KY를 최대한 잘 합치기 위한 데이터 전처리 과정 
      1-3. 중복을 제거하여 DB 적재
   
### 2. 인기차트 수집 자동화
> TJ, KY TOP 100 인기차트 데이터 수집 -> postgresql DB 적재

      2-1. 일주일 간격으로 최신화되는 인기차트

### 3. 로그 데이터 적재 (redis -> mongoDB) 자동화
> 실제 User들이 추천을 클릭 -> redis에 User의 플레이리스트 저장 -> mongoDB에 적재

      3-1. 하루 간격으로 로그 적재 (redis -> mongo)  
      3-2. 해당 날짜 기준 어제 적재된 값들만 mongoDB로 적재

### 4. 모델 재학습 자동화
> mongoDB에 저장된 값 -> gpu container(k-ict) -> model 재학습

      4-1. 하루 간격으로 모델 업데이트
      4-2. Airflow에 SSH connector 등록 후 통신

https://oh-um.tistory.com/29

### 5. FastAPI 모델 저장
>  fastapi에 python 파일 실행 시키기 (https://github.com/OhJune/Client-Django-FastAPI)

      5-1. python파일 내용: 구글 버킷에 있는 모델 저장하기 
      5-2. gcp fastapi vm인스턴스에 SSH connector 등록 후 통신


