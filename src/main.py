import uvicorn
from fastapi import FastAPI

from db.base import database
from endpoints import api

app = FastAPI(title="Youla API")
app.include_router(api)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
