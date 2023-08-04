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
SQLite_DIR = f"../../datas/SQLite/{sensor_id}"
mysql_config = {
    'host': '34.22.92.176',
    'user': 'root',
    'password': 'hanul0702',
    'port':'3306',
    'db': 'hanul_site'
}

# UPDATE DATABASE
#lib.JSON_to_table(JSON_DIR, TABLE_NAME)
lib.SQLite_to_MySQL(SQLite_DIR, mysql_config, TABLE_NAME)