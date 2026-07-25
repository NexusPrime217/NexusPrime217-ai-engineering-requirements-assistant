from pydantic import BaseModel

class LoginRequest(BaseModel):
    username:str
    password:str

class LoginResponse(BaseModel):
    username:str
    email:str
    token:str
