from fastapi import FastAPI
from routers import load_SQLite, load_check_DONE_flag

app = FastAPI()
app.include_router(load_SQLite.router)
app.include_router(load_check_DONE_flag.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=9000)
