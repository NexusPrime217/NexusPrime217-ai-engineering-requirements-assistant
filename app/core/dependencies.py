from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.core import jwt_util
from app.database.database import get_db
from app.model.user import User as userDB
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(access_token : str = Depends(oauth2_scheme),
                     db : Session = Depends(get_db)) -> userDB:
    claims = jwt_util.decode_access_token(access_token)

    sub = claims["sub"]
    print(sub)
    user_from_db = db.query(userDB).filter(userDB.id == sub).first()
    if user_from_db is None:
        raise HTTPException(status_code=401,
                            detail="Invalid authentication credentials")
    return user_from_db

