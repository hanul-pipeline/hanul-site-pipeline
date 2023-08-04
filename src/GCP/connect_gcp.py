# pip install google-cloud-storage

import os
from google.cloud import storage
from google.oauth2 import service_account

### GCP 연동 방법 1 ###
# KEY_PATH : GCP 사용자 계정 크레덴셜 키 경로(JSON형식)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="KEY_PATH"

# 버켓 목록 확인
storage_client = storage.Client()
buckets = list(storage_client.list_buckets())

print(buckets)

### GCP 연동 방법 2 ###
# 서비스 계정 인증 정보가 담긴 JSON 파일 경로
KEY_PATH = "./config/key.json"
# Credentials 객체 생성
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
# 구글 스토리지 클라이언트 객체 생성
client = storage.Client(credentials = credentials, project = credentials.project_id)



# GCP에 파일 올리기
bucket_name = ''    # 서비스 계정 생성한 bucket 이름 입력
source_file_name = ''    # GCP에 업로드할 파일 절대경로
destination_blob_name = ''    # 업로드할 파일을 GCP에 저장할 때의 이름


storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(source_file_name)

# GCP에서 파일 다운로드
bucket_name = ''    # 서비스 계정 생성한 bucket 이름 입력
source_blob_name = ''    # GCP에 저장되어 있는 파일 명
destination_file_name = ''    # 다운받을 파일을 저장할 경로("local/path/to/file")

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)

blob.download_to_filename(destination_file_name)