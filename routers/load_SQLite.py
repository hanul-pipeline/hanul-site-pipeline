from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_SQLite import *
from datetime import datetime

router = APIRouter()
@router.post('/sensor', response_class=PlainTextResponse)
async def receive_data(data_received: dict):
    # <CONTAINER DIR>
    data_DIR = "/hanul/datas/"
    return insert_measurements(data_received, data_DIR)
