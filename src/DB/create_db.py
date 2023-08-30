from datetime import datetime, timedelta
import configparser, sqlite3

config = configparser.ConfigParser()
config.read("/hanul/config/config.ini")
config.read("/Users/kimdohoon/git/hanul/hanul-site-pipeline/config/config.ini") # test
sensor_list = config.get("Sensor", "sensor_list")
sensors = [str(sensor) for sensor in sensor_list.split(',')]

date = (datetime.now() + timedelta(hours=1)).strftime("%y%m%d_%H")
print(date)

for sensor in sensors:
    path = f"/hanul/datas/SQLite/{sensor}/{date}_{sensor}"
    path = f"/Users/kimdohoon/git/hanul/hanul-site-pipeline/datas/SQLite/{sensor}/{date}_{sensor}" # test

    with open(path, "w") as file:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

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