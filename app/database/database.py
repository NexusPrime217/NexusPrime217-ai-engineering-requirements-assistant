from sqlalchemy import create_engine,URL
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import setting
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

connection_url=URL.create(
    drivername=setting.DRIVER_NAME,
    username=setting.DB_USERNAME,
    password=setting.DB_PASSWORD,
    host=setting.DB_HOST,
    port=setting.DB_PORT,
    database=setting.DB_NAME
)

def get_db() -> Session:
    db=session()
    try:
        yield db
    finally:
        db.close()

engine = create_engine(connection_url,echo=True)
session = sessionmaker(bind = engine, autoflush = False, autocommit = False)
