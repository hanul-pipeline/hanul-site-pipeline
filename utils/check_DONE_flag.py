import glob
from datetime import datetime, timedelta

def check_flag(FLAG_DIR:str, check_time:int, interval:int):
    # 현재 시간과 한 시간 전 시간을 계산
    now = datetime.now().replace(minute=0, second=0, microsecond=0) # 현재 시간을 추출해서 정각으로 변환
    one_hour_ago = now - timedelta(hours=1)
    
    # 테스트 설정
    #now = datetime(2023, 7, 24, 20, 0, 0)
    #one_hour_ago = now - timedelta(hours=1)

    valid_files = int(check_time / interval) # 1시간 / interval의 값으로 기대되는 파일 수를 계산
    
    # 디렉토리 안의 모든 json 파일을 읽음
    file_count = 0 # 실제 파일 수를 세는 변수
    for filename in glob.glob(FLAG_DIR + '/*'):
        # 파일명에서 시간 정보를 추출
        timestamp_str = filename.split('/')[-1].split('&')[1] + '&' + filename.split('/')[-1].split('&')[2]  # 'date&time' 형식
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d&%H:%M:%S')  # 날짜와 시간 형식에 따라서 수정해야 함

        # 파일의 시간이 한 시간 전과 현재 사이에 있는 경우에만 처리
        if one_hour_ago <= timestamp < now:
            file_count += 1
    
    return (f"Data Integrity Check : {file_count == valid_files}\n")
    # 테스트 설정        
    # return file_count == valid_files, file_count, valid_files, now, one_hour_ago

# 테스트 설정
# LOG_DIR = f"/home/kjh/code/hanul-site-pipeline/datas/DONE/1"
# check_time = 3600
# interval = 1

# result, file_count, valid_files, now, one_hour_ago = check_flag(LOG_DIR, check_time, interval)
# print(result, file_count, valid_files, now, one_hour_ago)

# check_flag 파라미터 샘플
# LOG_DIR = f"/home/kjh/code/hanul-site-pipeline/datas/DONE/{sensor_id}"
# check_time = 3600
# interval = 1
