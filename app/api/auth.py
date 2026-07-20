from fastapi import HTTPException

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.database.database import session
from app.schemas import UserCreate, UserResponse
from app.services import auth_service

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


# router.post("/login")
#
#
# router.post("/logout")
#
#
# router.get("/me")

