from fastapi import APIRouter, Depends
from app.database.database import session
from app.schemas import UserResponse
from app.model.user import User as userDB
from app.schemas.user import UserUpdate
from app.services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=UserResponse)
def get_users(db=Depends(get_db)):
    return db.query(userDB).all()

@router.get("/{user_id}", response_model=UserResponse)
def get_users_by_id(user_id:int, db=Depends(get_db)):
    return db.get(userDB,user_id)

@router.patch("/{user_id}", response_model=UserResponse)
def update_user_by_id(user_id:int,
                      user: UserUpdate,
                      db=Depends(get_db)):
    return user_service.update_user(user_id, user, db)

@router.patch("/password/{user_id}")
def update_password_by_id(user_id:int,
                          password:str,
                          db=Depends(get_db)):
    return user_service.update_user_password(user_id,password,db)


@router.delete("/{user_id}")
def delete_user(user_id:int,
                db=Depends(get_db)):
    return user_service.delete_user(user_id,db)