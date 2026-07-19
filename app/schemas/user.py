from datetime import datetime
from pydantic import EmailStr
from pydantic import BaseModel, ConfigDict, Field


from app.schemas.roles import Roles


class UserCreate(BaseModel):
    username:str = Field(min_length=3, max_length=20)
    password:str = Field(min_length=5, max_length=20)
    email:EmailStr
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    role: Roles

class UserResponse(BaseModel):
    id: int
    username: str
    role: Roles

    model_config = ConfigDict(from_attributes=True)
