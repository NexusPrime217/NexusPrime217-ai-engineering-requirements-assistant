from fastapi import FastAPI
from app.core.config import Settings
from app.database.database import session, engine, Base
from app.schemas import UserCreate, Roles
from app.model.user import User as userDB

setting = Settings()
app = FastAPI(title=setting.APP_NAME,
    version=setting.APP_VERSION,
    description=setting.APP_DESCRIPTION,
    debug=setting.DEBUG)

Base.metadata.create_all(bind=engine)

user=UserCreate(username="User1",
                password="pass123",
                role=Roles.USER)
@app.get("/")
def home_page():
    return "Hello world!"

@app.get("/db")
def db_connection():
    db=session()
    db.add(userDB(**user.model_dump()))
    db.commit()

# db_connection()
