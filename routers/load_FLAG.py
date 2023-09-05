from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.check_FLAG import *
from datetime import datetime

router = APIRouter()
@router.get('/flags/404', response_class=PlainTextResponse)
async def receive_flags():
    #FLAG_DIR = "/hanul/datas/"
    FLAG_DIR = "/home/kjh/code/hanul-site-pipeline/datas"
    check_time = 13
    interval = 1
    return check_flag(check_time, interval, FLAG_DIR)

@router.get("/test")
async def test():
    return {"message": "Test is successful!"}

