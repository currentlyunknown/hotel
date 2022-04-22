from fastapi import FastAPI

from hotel.db.create_db import create_db
from hotel.db.engine import init_db
from hotel.routers import bookings, customers, rooms
from settings import SQLALCHEMY_DATABASE_URI

app = FastAPI()

create_db(SQLALCHEMY_DATABASE_URI)


@app.on_event("startup")
def startup_event():
    init_db(SQLALCHEMY_DATABASE_URI)


@app.get("/")
def read_root():
    return "The server is running."


app.include_router(customers.router)
app.include_router(rooms.router)
app.include_router(bookings.router)
