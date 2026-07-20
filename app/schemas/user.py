from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field,EmailStr


from app.schemas.roles import Roles


class UserCreate(BaseModel):
    username:str = Field(min_length=3, max_length=20)
    password:str = Field(min_length=5, max_length=20)
    email:EmailStr
    role: Roles

class UserResponse(BaseModel):
    id: int
    username: str
    email:EmailStr
    role: Roles

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr


