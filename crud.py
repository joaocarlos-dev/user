from fastapi import HTTPException
from sqlalchemy.orm import Session
import model
import schema


def get_user_by_user_id(db: Session, user_id: str):
    return db.query(model.User).filter(model.User.user_id == user_id).first()


def get_user_by_id(db: Session, u_id: int):
    return db.query(model.User).filter(model.User.id == u_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def add_user(db: Session, user: schema.UserAdd):
    
    user_details = model.User(
        user_id=user.user_id,
        name=user.name,
        email=user.email,
        cpf=user.cpf,
        pis=user.pis,
        password=user.password,
        country = user.country,
        state = user.state,
        city = user.city,
        street = user.city,
        number = user.number,
        complement = user.complement
    )
    db.add(user_details)
    db.commit()
    db.refresh(user_details)
    return model.User(**user.dict())


def update_user(db: Session, u_id: int, details: schema.UpdateUser):
    db_user = db.query(model.User).filter(model.User.id == u_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.query(model.User).filter(model.User.id == u_id).update(vars(details))
    db.commit()
    return db.query(model.User).filter(model.User.id == u_id).first()


def delete_user(db: Session, u_id: int):
    try:
        db.query(model.User).filter(model.User.id == u_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)