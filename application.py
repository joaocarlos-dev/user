
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine
import uvicorn

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Users",
    description="PontoTel Users",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_users', response_model=List[schema.User])
def retrieve_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@app.post('/add_new_user', response_model=schema.UserAdd)
def add_new_user(user: schema.UserAdd, db: Session = Depends(get_db)):
    user_id = crud.get_user_by_user_id(db=db, user_id=user.user_id)
    if user_id:
        raise HTTPException(status_code=400, detail=f"User id {user.user_id} already exist in database: {user_id}")
    return crud.add_user(db=db, user=user)


@app.delete('/delete_user_by_id')
def delete_user_by_id(u_id: int, db: Session = Depends(get_db)):
    details = crud.get_user_by_id(db=db, u_id=u_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_user(db=db, u_id=u_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_user', response_model=schema.User)
def update_user_details(u_id: int, update_param: schema.UpdateUser, db: Session = Depends(get_db)):
    details = crud.get_user_by_id(db=db, u_id=u_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_user(db=db, details=update_param, u_id=u_id)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)