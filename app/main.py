from fastapi import FastAPI
from app.core.config import Settings
from app.database.database import  engine, Base
from app.api import user
from app.api import auth

import os

print(__file__)

setting = Settings()
app = FastAPI(title=setting.APP_NAME,
    version=setting.APP_VERSION,
    description=setting.APP_DESCRIPTION,
    debug=setting.DEBUG)

Base.metadata.create_all(bind=engine)

# user=UserCreate(username="User1",
#                 password="pass123",
#                 email="abc@gmail.com",
#                 role=Roles.USER)

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def home_page():
    return "Hello world!"




