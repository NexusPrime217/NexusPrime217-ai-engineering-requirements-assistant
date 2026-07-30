from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

print("SECRETKEY =", os.environ.get("SECRETKEY"))
print("API_KEY =", os.environ.get("API_KEY"))


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    SECRET_KEY: str
    APP_NAME : str
    APP_VERSION : str
    APP_DESCRIPTION : str
    DEBUG : bool
    DB_USERNAME: str
    DB_PASSWORD: str
    DRIVER_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    JWT_ALG:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    DOCUMENT_PATH:str
    LLM_MODEL: str


    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

setting = Settings()