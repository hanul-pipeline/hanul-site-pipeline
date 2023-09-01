from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse
from utils.check_FLAG import *
from datetime import datetime

router = APIRouter()
@router.post('/flags/404', response_class=PlainTextResponse)
async def receive_flags(data_received: dict):
    FLAG_DIR = "/hanul/datas/"
    return check_flag(data_received, FLAG_DIR)

@router.get("/test")
async def test():
    return {"message": "Test is successful!"}