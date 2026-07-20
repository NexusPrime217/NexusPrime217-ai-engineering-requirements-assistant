from http import HTTPStatus
from app.model import User as userDB
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserResponse
import bcrypt


def _hash_password(password : str):
    salt = bcrypt.gensalt()
    bytes = password.encode("utf-8")
    return bcrypt.hashpw(bytes,salt)


def register_user(user:UserCreate,db:Session):
    if db.query(userDB).filter(userDB.email == user.email).first():
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="email is already registered")
    if db.query(userDB).filter(userDB.username == user.username).first():
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="user is already taken")

    new_user = userDB(**user.model_dump())
    new_user.password=_hash_password(user.password)

    db.add(new_user)
    db.commit()

    return UserResponse.model_validate(new_user)