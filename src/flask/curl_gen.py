import subprocess, time, random
from datetime import datetime

import random # TEST

def send_curl_every_second(sensor_id, sensor_value, interval):
    while True:
        # SEND DATA TYPE : curl -X POST -H "Content-Type: application/json" -d \
        # '{"sensor_id": 1, "date":"2023-07-03", "time":"20:04:30", "gas_level": 50}' \
        # http://192.168.70.89:9000/data-endpoint
        # 192.168.70.89
        subprocess.run([
            'curl', '-X', 'POST', 
            '-H', 'Content-Type: application/json', 
            '-d',f'{{"sensor_id": {sensor_id}, "date":"{datetime.now().strftime("%Y-%m-%d")}", "time":"{datetime.now().strftime("%H:%M:%S")}", "measurement": {sensor_value}}}', 
            'http://192.168.254.36:9000/data-endpoint'
        ])
        time.sleep(interval)  # n초 동안 대기

# 함수 실행
if __name__ == "__main__":
    sensor_id = 404
    sensor_value = 500 * random.random()
    interval = 1
    send_curl_every_second(sensor_id, sensor_value, interval)
