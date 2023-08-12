# routers
: 엔드포인트에서 사용될 함수들을 매핑

# import modules
``` python
from fastapi import APIRouter, Request, Query
```

# .py structure

### main
``` python
router = APIRouter()

@router.get("/<end>/<point>/")
async def <function_name>(<var>:<type>):
    return <import_module_name>(<var>, <var>)
```

### example
``` python
import os
from fastapi import APIRouter, Request, Query
from utils.scout_modules import *
from urllib.parse import unquote

router = APIRouter()

@router.get("/done-flag/")
async def flag_check_data(target_dir:str):
    return check_flag_directory(target_dir)
```