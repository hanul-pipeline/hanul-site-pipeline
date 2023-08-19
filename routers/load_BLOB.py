from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse
from utils.BLOB import *
from datetime import datetime

router = APIRouter()
@router.post('/blob/404', response_class=PlainTextResponse)
async def receive_flags(data_received: dict):
    data_received_dict = data_received
    SQLite_DIR = "/home/kjh/code/hanul-site-pipeline/datas"
    return SQLite_to_datalake(data_received_dict, SQLite_DIR)

@router.get("/test")
async def test():
    return {"message": "Test is successful!"}