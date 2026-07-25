from fastapi import APIRouter, Depends
from app.database.database import get_db
from app.schemas import UserResponse
from app.model.user import User as userDB
from app.schemas.user import UserUpdate
from app.services import user_service
from app.core.dependencies import require_admin

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("", response_model=list[UserResponse])
def get_users(db=Depends(get_db),
              admin: userDB = Depends(require_admin)):
    return user_service.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_users_by_id(user_id:int,
                    db=Depends(get_db),
                    admin: userDB = Depends(require_admin)):
    return user_service.get_user_by_id(user_id,db)


@router.patch("/{user_id}", response_model=UserResponse)
def update_user_by_id(user_id:int,
                      user: UserUpdate,
                      db=Depends(get_db),
                      admin: userDB = Depends(require_admin)):
    return user_service.update_user(user_id, user, db)

@router.patch("/password/{user_id}")
def update_password_by_id(user_id:int,
                          password:str,
                          db=Depends(get_db)):
    return user_service.update_user_password(user_id,password,db)


@router.delete("/{user_id}")
def delete_user(user_id:int,
                db=Depends(get_db),
                admin: userDB = Depends(require_admin)):
    return user_service.delete_user(user_id,db)