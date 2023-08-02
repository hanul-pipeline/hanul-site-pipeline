 # MODULE IMPORT
from flask import Flask, request

# LIBRARY IMPORT
import os, sys
os.chdir('/flask_compose')
lib_dir = f"{os.getcwd()}/lib"
sys.path.append(lib_dir)
from MySQL.connector_lib import *
from processing.rank import *

# 
SQLite_DIR = '/flask_compose/datas/SQLite/cite'

# CREATE APP
app = Flask(__name__)

# BUILD APP
@app.route('/data-endpoint', methods=['POST'])
def receive_data():
    # MAKE DATA
    data_received = request.get_json()
    sensor_id = data_received["sensor_id"]
    date = data_received["date"]
    time = data_received["time"]
    measurement = data_received["measurement"]
    rank = determine_rank(sensor_id, measurement)

    # RANK INFORMATION UPDATE
    data_received["rank"] = rank
    QUERY = f"""
        INSERT INTO sensor_data (sensor_id, date, time, measurement, rank)
        VALUES ({sensor_id}, '{date}', '{time}', {measurement}, '{rank}')
        """

    # INSERT DATAS INTO SQLITE + CREATE FLAG
    SQLite_UPDATE(SQLite_DIR, QUERY)
    LOG_DIR = f"/flask_compose/datas/DONE/{sensor_id}"

    # CREATE FLAG
    with open(f"{LOG_DIR}/{sensor_id}&{date}&{time}&DONE", "w") as file:
            pass

    # END
    return(f"DATA RECEIVED {time}\n")

# RUN APP
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)