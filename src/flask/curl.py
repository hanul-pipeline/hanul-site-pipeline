# CHANGE WORK DIR
import os
os.chdir('/Users/kimdohoon/git/hanul/hanul-site-pipeline')
# os.chdir("컨테이너 디렉토리")
now_dir = os.getcwd()

# MODULE IMPORT
from datetime import datetime
from flask import Flask, request
import json

# CREATE APP
app = Flask(__name__)

# BUILD APP
@app.route('/data-endpoint', methods=['POST'])
def receive_data():
    # MAKE DATA
    data_received = request.get_json()
    print(data_received)
    sensor_id = data_received["sensor_id"]
    date = data_received["date"]
    time = data_received["time"]

    # CREATE JSON FILE
    DATA_DIR = f"{now_dir}/datas/JSON/{sensor_id}"
    LOG_DIR = f"{now_dir}/datas/DONE/{sensor_id}"

    with open(f"{DATA_DIR}/{sensor_id}&{date}&{time}.json", "w") as file:
        json.dump(data_received, file, indent=4)
        with open(f"{LOG_DIR}/{sensor_id}&{date}&{time}&DONE", "w") as file:
            pass

    # END
    return("DATA RECEIVED")

# RUN APP
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)