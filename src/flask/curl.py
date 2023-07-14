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
    # date = datetime.now().strftime("%Y-%m-%d")
    # time = datetime.now().strftime("%H:%M:%S")
    data_received = request.get_json()
    sensor_id = data_received["sensor_id"]
    date = data_received["date"]
    time = data_received["time"]
    # data = {"date" : date}
    # for key, value in data_received.items():
    #     data[key] = value

    # CREATE JSON FILE
    DATA_DIR = f"../../datas/JSON/{sensor_id}"
    LOG_DIR = f"../../datas/DONE/{sensor_id}"

    with open(f"{DATA_DIR}/{sensor_id}&{date}&{time}.json", "w") as file:
        # json.dump(data, file, indent=4)
        json.dump(data_received, file, indent=4)
        # CREATE FLAG
        with open(f"{LOG_DIR}/{sensor_id}&{date}&{time}&DONE", "w") as file:
            pass

    # END
    return("DATA RECEIVED")

# RUN APP
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)