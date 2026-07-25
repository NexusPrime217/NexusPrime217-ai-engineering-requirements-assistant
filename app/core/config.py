from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
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
    # SECRETKEY: str
    JWT_ALG:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

setting = Settings()