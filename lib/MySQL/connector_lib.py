import mysql.connector, sqlite3
import csv, json
import glob
from datetime import datetime, timedelta

'''
SQLite Modules
'''
# CREATE CONNECTIONS & CURSORS - SQLite
def SQLite_UPDATE(PATH, QUERY):
    connection = sqlite3.connect(PATH)
    cursor = connection.cursor()
    cursor.execute("PRAGMA journal_mode = WAL")
    cursor.execute(QUERY)
    connection.commit()

def transfer_data(sqlite_path, mysql_config, table_name):
    # SQLite DB에 연결
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    # 현재 시간과 한 시간 전 시간을 계산
    now = datetime.now().replace(minute=0, second=0, microsecond=0) # 현재 시간을 추출해서 정각으로 변환
    one_hour_ago = now - timedelta(hours=1)
    one_hour_ago_str = one_hour_ago.strftime('%Y-%m-%d %H:%M:%S')

    # SQLite DB에서 지난 한 시간의 데이터를 가져옴
    cursor.execute(f"SELECT * FROM {table_name} WHERE date || ' ' || time > ?", (one_hour_ago_str,))
    rows = cursor.fetchall()

    # MySQL DB에 연결
    mysql_conn = mysql.connector.connect(**mysql_config)
    mysql_cursor = mysql_conn.cursor()

    # MySQL DB에 데이터 삽입
    for row in rows:
        # 이 부분은 실제 필드에 맞게 수정해야 합니다.
        mysql_cursor.execute(
            f"INSERT INTO {table_name} (id, sensor_id, date, time, measurement, `rank`) VALUES (%s, %s, %s, %s, %s, %s)",
            row
        )

    # MySQL DB 연결 종료
    mysql_conn.commit()
    mysql_cursor.close()
    mysql_conn.close()

    # SQLite DB 연결 종료
    cursor.close()
    conn.close()

# 사용 예
sqlite_file = "/home/kjh/code/hanul-site-pipeline/datas/SQLite/cite"
mysql_config = {
    'host': 'localhost',
    'user': 'kjh',
    'password': '1111',
    'port':'3307',
    'db': 'kjh'
}
table_name = "sensor_data"
transfer_data(sqlite_file, mysql_config, table_name)



'''
MySQL Modules
'''

# # CSV File Located At Local
# PATH_DB = '/Users/kimdohoon/src/google/hanul_sql.csv'
# with open(PATH_DB, 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         db_data = row
# # CREATE CONNECTIONS & CURSORS
# def MySQL_CONNECT():
#     conn = mysql.connector.connect(
#         host=row[0],
#         user=row[1],
#         password=row[2],
#         database="hanul_site"
#     )
#     return conn





# # UPDATE DATABASE VER.2
# def MySQL_UPDATE(JSON_DIR, TABLE_NAME):
#     conn = MySQL_CONNECT()
#     cursor = conn.cursor()
#     # 현재 시간과 한 시간 전 시간을 계산
#     now = datetime.now().replace(minute=0, second=0, microsecond=0) # 현재 시간을 추출해서 정각으로 변환
#     one_hour_ago = now - timedelta(hours=1)

#     DB_LOG_DIR = f"../../datas/DONE/...." # 센서ID 기준? 매 시간 기준?
    
#     # 디렉토리 안의 모든 json 파일을 읽음
#     for filename in glob.glob(JSON_DIR):
#         # 파일명에서 시간 정보를 추출
#         timestamp_str = filename.split('/')[-1].split('&')[1] + '&' + filename.split('/')[-1].split('&')[2].split('.')[0]  # 'date&time' 형식
#         timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d&%H:%M:%S')  # 날짜와 시간 형식에 따라서 수정해야 함

#         # 파일의 시간이 한 시간 전과 현재 사이에 있는 경우에만 처리
#         if one_hour_ago <= timestamp < now:
#             with open(filename, 'r') as f:
#                 # json 파일을 파싱
#                 data = json.load(f)

#                 # MySQL 쿼리 생성
#                 sql = f"INSERT INTO {TABLE_NAME}(sensor_id, date, time, value) VALUES (%s, %s, %s, %s)"
#                 cursor.execute(sql, (data['sensor_id'], data['date'], data['time'], data['value']))
                
#                 # DB DONE FLAG 생성
#                 with open(f"{DB_LOG_DIR}/{data['sensor_id']}&{one_hour_ago}&DONE", "w") as file:
#                     pass
        
#     conn.commit()
    
#     # 