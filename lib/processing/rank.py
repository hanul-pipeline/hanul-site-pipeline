from decimal import Decimal

# 추후 센서 데이터 등급 세분화 필요

def determine_rank(sensor_id, measurement):
    print(type(measurement))
    measurement = Decimal(measurement)
    if sensor_id == 1:
        if measurement <= 2:
            return "P"
        else:
            return "D"
    if sensor_id == 2:
        if measurement <= 2.1:
            return "P"
        else:
            return "D"