from datetime import datetime, timezone, timedelta
from http import HTTPStatus
from app.model import User as userDB
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserResponse
from app.model.auth import LoginRequest, LoginResponse
from app.core.config import Settings
from app.core import jwt_util
import bcrypt


def _hash_password(password : str) -> str:
    salt = bcrypt.gensalt()
    password_bytes = password.encode("utf-8")
    return bcrypt.hashpw(password_bytes,salt).decode("utf-8")

def _verify_password(plain_password,
                     hashed_password)->bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"),
                          hashed_password.encode("utf-8"))



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


def login_user(creds:LoginRequest, db:Session)->LoginResponse:
    user_from_db = db.query(userDB).filter(userDB.username == creds.username).first()
    if not user_from_db:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail="username or password is incorrect")

    if not _verify_password(creds.password, user_from_db.password):
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail="username or password is incorrect")


    payload = {
        "sub" : str(user_from_db.id),
        "role" : user_from_db.role,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    access_token = jwt_util.create_access_token(payload)

    return LoginResponse(username = user_from_db.username,
                         email = user_from_db.email,
                         token = access_token)





