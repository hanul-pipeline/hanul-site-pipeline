import mysql.connector, json, csv
import glob
from datetime import datetime, timedelta

# CSV File Located At Local
PATH_DB = '/Users/kimdohoon/src/google/hanul_sql.csv'
with open(PATH_DB, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        db_data = row

# CREATE CONNECTIONS & CURSORS
def mysql_connect():
    conn = mysql.connector.connect(
        host=row[0],
        user=row[1],
        password=row[2],
        database="hanul_site"
    )
    return conn

# UPDATE DATABASE
def JSON_to_table(JSON_DIR, TABLE_NAME):
    conn = mysql_connect()
    cursor = conn.cursor()
    with open(JSON_DIR) as file:
        data = json.load(file)
    sensor_id = data['sensor_id']
    date = data['date']
    time = data['time']
    value = data['value']
    query = f"INSERT INTO {TABLE_NAME} (sensor_id, date, time, value) \
              VALUES ({sensor_id}, {date}, {time}, {value})"
    cursor.execute(query)
    conn.commit()
    
# UPDATE DATABASE VER.2
def JSON_to_table_ver2(JSON_DIR, TABLE_NAME):
    conn = mysql_connect()
    cursor = conn.cursor()
    # 현재 시간과 한 시간 전 시간을 계산
    now = datetime.now().replace(minute=0, second=0, microsecond=0) # 현재 시간을 추출해서 정각으로 변환
    one_hour_ago = now - timedelta(hours=1)

    DB_LOG_DIR = f"../../datas/DONE/...." # 센서ID 기준? 매 시간 기준?
    
    # 디렉토리 안의 모든 json 파일을 읽음
    for filename in glob.glob(JSON_DIR):
        # 파일명에서 시간 정보를 추출
        timestamp_str = filename.split('/')[-1].split('&')[1] + '&' + filename.split('/')[-1].split('&')[2].split('.')[0]  # 'date&time' 형식
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d&%H:%M:%S')  # 날짜와 시간 형식에 따라서 수정해야 함

        # 파일의 시간이 한 시간 전과 현재 사이에 있는 경우에만 처리
        if one_hour_ago <= timestamp < now:
            with open(filename, 'r') as f:
                # json 파일을 파싱
                data = json.load(f)

                # MySQL 쿼리 생성
                sql = f"INSERT INTO {TABLE_NAME}(sensor_id, date, time, value) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (data['sensor_id'], data['date'], data['time'], data['value']))
                
                # DB DONE FLAG 생성
                with open(f"{DB_LOG_DIR}/{data['sensor_id']}&{one_hour_ago}&DONE", "w") as file:
                    pass
        
    conn.commit()
    
    # 