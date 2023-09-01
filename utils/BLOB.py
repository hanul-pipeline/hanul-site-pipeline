from google.cloud import storage
from google.oauth2 import service_account
import os
import glob
from datetime import datetime, timedelta

# 전 날 쌓인 SQLite 데이터를 DATALAKE로 보내기
def SQLite_to_datalake(sensor_id: str):
    bucket_name = "hanul-sensors"
    GCS_DIR = '/hanul/datas'
    SQLite_DIR = "/home/kjh/code/hanul-site-pipeline/datas"
    
    ### GCP 연동 방법 2 ###
    # 서비스 계정 인증 정보가 담긴 JSON 파일 경로
    KEY_PATH = "/home/kjh/.GCS/watchful-cirrus-392405-6443a1b86f94.json"
    # Credentials 객체 생성
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    # 구글 스토리지 클라이언트 객체 생성
    storage_client = storage.Client(credentials = credentials, project = credentials.project_id)
    bucket = storage_client.bucket(bucket_name)

    # 현재 시간과 한 시간 전 시간을 계산
    now = datetime.now().replace(minute=0, second=0, microsecond=0) # 현재 시간을 추출해서 정각으로 변환
    one_hour_ago = now - timedelta(hours=1)
    
    messages = []
    # 디렉토리 안의 모든 SQLite 파일을 읽음
    for filename in glob.glob(f"{SQLite_DIR}/SQLite/*"):
        # 파일명에서 시간 정보를 추출 (파일명은 yyyymmdd_hh_sensorid 형식)
        timestamp_str = filename.split('/')[-1].split('_')[0] + '_' + filename.split('/')[-1].split('_')[1]  # 'yyyymmdd_HH' 형식
        timestamp = datetime.strptime(timestamp_str, '%Y%m%d_%H')  # 날짜와 시간 형식에 따라서 수정해야 함
        file_sensor_id = filename.split('/')[-1].split('_')[2]
        
        # 파일의 시간이 한 시간 전과 현재 사이에 있는 경우에만 처리
        if file_sensor_id == sensor_id and one_hour_ago <= timestamp < now:
            destination_blob_name = os.path.join(GCS_DIR, os.path.basename(filename))
            blob = bucket.blob(destination_blob_name)
            try:
                blob.upload_from_filename(filename)
                messages.append(f"File {filename} uploaded to {GCS_DIR}.")
            except Exception as e:
                messages.append(f"Failed to upload {filename}. Error: {e}")
    return '\n'.join(messages)

#if __name__ == '__main__':
#    # 테스트를 위한 데이터
#    data_received = {
#        "bucket_name": "hanul-sensors",
#        "GCS_DIR": "404/"
#    }
#    SQLite_DIR = "/home/kjh/code/hanul-site-pipeline/datas"  # 실제 SQLite 파일들이 있는 디렉토리로 수정해주세요
#
#    result = SQLite_to_datalake(data_received, SQLite_DIR)
#    print(result)
