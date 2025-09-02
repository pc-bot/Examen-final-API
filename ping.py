from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def get_Ping():
    return "pong"