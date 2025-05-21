import uvicorn
from fastapi import FastAPI

from app.bookings.router import router as router_bookings

app = FastAPI()

#вставка своего роутера
app.include_router(router_bookings)


@app.get("/")
async def root():
    return {"message": "Привет, мир"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)