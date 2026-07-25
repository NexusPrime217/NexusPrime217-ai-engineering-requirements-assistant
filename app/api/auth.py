from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.model.auth import LoginRequest, LoginResponse
from app.database.database import session
from app.schemas import UserCreate, UserResponse
from app.services import auth_service
from app.model.user import User as userDB
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

def get_db() -> Session:
    db=session()
    try:
        yield db
    finally:
        db.close()



@router.post("/register", response_model=UserResponse)
def register_user(user:UserCreate,db=Depends(get_db)):
    return auth_service.register_user(user,db)


@router.post("/login", response_model=LoginResponse)
def login_user(creds:LoginRequest, db=Depends(get_db)):
    return auth_service.login_user(creds, db)

#
# router.post("/logout")
#
#
@router.get("/me",response_model=UserResponse)
def me(current_user : userDB = Depends(get_current_user)):
    return current_user

