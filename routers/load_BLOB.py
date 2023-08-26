from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse
from utils.BLOB import *
from datetime import datetime

router = APIRouter()
@router.post('/blob/404', response_class=PlainTextResponse)
async def receive_flags():
    sensor_id = '404'
    return SQLite_to_datalake(sensor_id)

@router.get("/test")
async def test():
    return {"message": "Test is successful!"}