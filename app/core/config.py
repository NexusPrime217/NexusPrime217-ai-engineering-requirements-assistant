from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    app_name : str
    app_version : str
    app_description : str
    debug : bool

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

