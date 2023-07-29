# MODULE IMPORT
import sys
sys.path.append('../../lib/MySQL')
import connector_lib as lib
import check_flag as etc

# LOGIC - DONE FLAG
# DONE FLAG 에서 시간이 해당 시간인 데이터 추려서 개수 파악하기
# 개수 비교하기
# 비교 끝나면 JSON 들어가서 해당 시간인 데이터 추리기
# 그 데이터들만 읽어서 서버에 올리기

# PARAMETERS
sensor_id = sys.argv[1]
check_time = sys.argv[2] # 1시간 기준(3600). 센서마다 상이?
interval = sys.argv[3] # 센서마다 상이
JSON_DIR = f"../../datas/JSON/{sensor_id}"
TABLE_NAME = 'measurement'


# UPDATE DATABASE
# lib.JSON_to_table(JSON_DIR, TABLE_NAME)

# CHECK FLAG
check = etc.check_flag(JSON_DIR, check_time, interval)

if check is True:
    # UPDATE DATABASE VER.2
    lib.JSON_to_table_ver2(JSON_DIR, TABLE_NAME)
