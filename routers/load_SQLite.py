from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_SQLite import *
from datetime import datetime

router = APIRouter()
@router.post('/sensors', response_class=PlainTextResponse)
async def receive_data(data_received: dict):
    # <CONTAINER DIR>
    #data_DIR = "/hanul/datas/"
    data_DIR = "/home/kjh/code/hanul-site-pipeline/datas"
    return insert_measurements(data_received, data_DIR)
