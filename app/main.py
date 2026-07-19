from typing import final

from fastapi import FastAPI
from fastapi.params import Depends

from app.core.config import Settings
from app.database.database import session, engine, Base
from app.schemas import UserCreate, Roles, UserResponse
from app.model.user import User as userDB

setting = Settings()
app = FastAPI(title=setting.APP_NAME,
    version=setting.APP_VERSION,
    description=setting.APP_DESCRIPTION,
    debug=setting.DEBUG)

# Base.metadata.create_all(bind=engine)

user=UserCreate(username="User1",
                password="pass123",
                email="abc@gmail.com",
                role=Roles.USER)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home_page():
    return "Hello world!"

@app.post("/init")
def db_connection(db=Depends(get_db)):
    db.add(userDB(**user.model_dump()))
    db.close()

# db_connection()

@app.get("/users/count")
def get_user_count(db=Depends(get_db)):
    total_users=db.query(userDB).count()
    return total_users

@app.get("/users")
def get_user_count(db=Depends(get_db)):
    users=db.query(userDB).all()
    result=[UserResponse.model_validate(user) for user in users]
    return result

