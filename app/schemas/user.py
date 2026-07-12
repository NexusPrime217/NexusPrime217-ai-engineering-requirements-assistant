from pydantic import BaseModel, ConfigDict

from app.schemas.roles import Roles


class UserCreate(BaseModel):
    username:str
    password:str
    role: str

class UserResponse(BaseModel):
    id: int
    username: str
    role: Roles

    model_config = ConfigDict(from_attributes=True)
