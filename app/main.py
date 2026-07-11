from fastapi import FastAPI

from app.core.config import Setting

setting = Setting()
app = FastAPI(title=setting.app_name,
    version=setting.app_version,
    description=setting.app_description,
    debug=setting.debug)

@app.get("/")
def home_page():
    return "Hello world!"