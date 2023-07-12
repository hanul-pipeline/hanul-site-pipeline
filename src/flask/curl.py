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
    date = datetime.now()
    data_received = request.get_json()
    sensor_id = data_received["sensor_id"]
    data = {"date" : date}
    for key, value in data_received.items():
        data[key] = value

    # CREATE JSON FILE
    DATA_DIR = "../../datas/JSON/404"
    LOG_DIR = "../../datas/DONE/404"
    with open(f"{DATA_DIR}/{sensor_id}-{date}.json", "w") as file:
        json.dump(data, file, indent=4)
        file.write(",")
        # CREATE FLAG
        with open(f"{LOG_DIR}/{sensor_id}-{date}-DONE", "w") as file:
            pass

    # END
    return("DATA RECEIVED")

# RUN APP
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)