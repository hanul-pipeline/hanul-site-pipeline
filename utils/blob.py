from google.cloud import storage
import os
import glob
from datetime import datetime, timedelta
import subprocess

# 전 날 쌓인 JSON 데이터를 DATALAKE로 보내기
def SQLite_to_datalake(bucket_name, SQLite_DIR, destination_blob_directory):
    # 구글 클라우드 스토리지 버켓정보
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    # 크론잡이 2023-07-15 00시에 실행될 경우 2023-07-14 데이터만 설정
    exe_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    # 해당 경로 내 JSON 파일 리스트
    files = glob.glob(os.path.join(SQLite_DIR, '*.json'))

    for file in files:
        # JSON파일에서 날짜 추출
        file_date = os.path.basename(file).split('&')[1]
        
        # 추출된 날짜와 보내야 할 날짜 비교
        if file_date != exe_date:
            continue
        
        destination_blob_name = os.path.join(destination_blob_directory, os.path.basename(file))
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(file)

        print(
            "File {} uploaded to {}.".format(
                file, destination_blob_name
            )
        )

# DATALAKE로 보낸 후 전전 날 JSON 데이터 삭제
def del_SQLite(SQLite_DIR):
    # 크론잡이 2023-07-15 00시에 실행될 경우 2023-07-13 데이터만 설정
    exe_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
    
    # 해당 경로 내 JSON 파일 리스트
    files = glob.glob(os.path.join(SQLite_DIR, '*.json'))

    for file in files:
        # JSON파일에서 날짜 추출
        file_date = os.path.basename(file).split('&')[1]
        
        # 추출된 날짜와 지워야 할 날짜 비교
        if file_date != exe_date:
            continue
        
        subprocess.run(['rm', f'{file}'])
        
SQLite_to_datalake('my_bucket','source_path','blob_path')
del_JSON('source_path')