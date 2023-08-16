from datetime import datetime, timedelta
# from libs.DB.SQLite import *
import configparser, sqlite3

config = configparser.ConfigParser()
# config.read("/hanul/config/config.ini")
config.read("/Users/kimdohoon/git/hanul/hanul-site-pipeline/config/config.ini")
sensor_list = config.get("Sensor", "sensor_list")
sensors = [str(sensor) for sensor in sensor_list.split(',')]

# yymmdd_HH_404
date = (datetime.now() + timedelta(hours=1)).strftime("%y%m%d_%H")
print(date)

for sensor in sensors:
    # 테스트 경로(로컬)
    path = f"/Users/kimdohoon/git/hanul/hanul-site-pipeline/datas/SQLite/{sensor}/{date}_{sensor}"
    # 실제 경로
    # path = f"/hanul/datas/SQLite/{sensor}/{date}_{sensor}"
    with open(path, "w") as file:
            # 데이터베이스 연결 생성 또는 기존 데이터베이스 연결
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

        # 테이블 생성 쿼리
        QUERY = '''
        CREATE TABLE IF NOT EXISTS measurement (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_id TEXT,
                date TEXT,
                time TEXT,
                measurement REAL,
                rank TEXT);
        '''
        cursor.execute(QUERY)
        conn.commit()