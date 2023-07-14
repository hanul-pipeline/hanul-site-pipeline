import subprocess
import time
from datetime import datetime

def send_curl_every_second():
    while True:
        subprocess.run([
            'curl', '-X', 'POST', 
            '-H', 'Content-Type: application/json', 
            '-d',f'{{"sensor_id": 1, "date":"{datetime.now().strftime("%Y-%m-%d")}", "time":"{datetime.now().strftime("%H:%M:%S")}", "gas_level": 50}}', 
            'http://192.168.70.89:9000/data-endpoint'
        ])
        time.sleep(1)  # 1초 동안 대기

# 함수 실행
send_curl_every_second()

