from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_SQLite import *
from datetime import datetime

router = APIRouter()
@router.post('/sensors', response_class=PlainTextResponse)
async def receive_data(data_received: dict):
    data_DIR = "/hanul/datas/"
    # SQLite_DIR = "/Users/kimdohoon/git/hooniegit/FastAPI-demo/datas/SQLite/sensors"
    return insert_measurements(data_received, data_DIR)
