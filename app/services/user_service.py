from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.user import User as userDB
from app.schemas import UserResponse
from app.schemas.user import UserUpdate


def update_user(user_id:int, user:UserUpdate, db:Session):
    db_user = db.query(userDB).filter(userDB.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404,
                            detail="User not found")

    update_data = user.model_dump(exclude_unset=True)

    for field,value in update_data.items():
        setattr(db_user,field,value)

    db.commit()
    db.refresh(db_user)

    return UserResponse.model_validate(db_user)


def update_user_password(user_id:int, password : str, db:Session):
    db_user = db.query(userDB).filter(userDB.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404,
                            detail="User not found")

    setattr(db_user,"password",password)

    db.commit()


    return "Password updated successfully"


def delete_user(user_id, db):
    db_user = db.query(userDB).filter(userDB.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404,
                            detail="User not found")

    db.delete(db_user)
    db.commit()

    return "User deleted"