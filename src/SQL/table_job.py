# MODULE IMPORT
import sys
sys.path.append('../../lib/MySQL')
import connector_lib as lib

# LOGIC - DONE FLAG
# DONE FLAG 에서 시간이 해당 시간인 데이터 추려서 개수 파악하기
# 개수 비교하기
# 비교 끝나면 JSON 들어가서 해당 시간인 데이터 추리기
# 그 데이터들만 읽어서 서버에 올리기

# SQLite_to_MySQL 파라미터
sensor_id = sys.argv[1]
# JSON_DIR = f"../../datas/JSON/{sensor_id}"
TABLE_NAME = 'measurement'
SQLite_DIR = f"../../datas/JSON/{sensor_id}"
mysql_config = {
    'host': 'localhost',
    'user': 'kjh',
    'password': '1111',
    'port':'3307',
    'db': 'kjh'
}
# check_flag 파라미터
LOG_DIR = f"/home/kjh/code/hanul-site-pipeline/datas/DONE/{sensor_id}"
check_time = 3600
interval = 1

# UPDATE DATABASE
#lib.JSON_to_table(JSON_DIR, TABLE_NAME)
check_done = check_flag(LOG_DIR, check_time, interval)
lib.SQLite_to_MySQL(SQLite_DIR, mysql_config, TABLE_NAME)