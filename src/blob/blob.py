from google.cloud import storage
import os
import glob

def JSON_to_datalake(bucket_name, source_directory, destination_blob_directory):
    # 구글 클라우드 스토리지 버켓정보
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    # 보내야 하는 JSON 파일 리스트
    files = glob.glob(os.path.join(source_directory, '*.json'))

    for file in files:
        destination_blob_name = os.path.join(destination_blob_directory, os.path.basename(file))
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(file)

        print(
            "File {} uploaded to {}.".format(
                file, destination_blob_name
            )
        )
JSON_to_datalake('my_bucket','source_path','blob_path')