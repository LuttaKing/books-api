from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schema
from database import SessionLocal, engine


# create tables in db
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.UserSchema)
def create_user(user: schema.UserSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schema.UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schema.UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {'message':f'succes deleted {db_user.email}' }
    

@app.put("/users/{user_id}")
def update_user(user_id: int,user: schema.UserSchema, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user=user)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {'message':f'succes updated {db_user.email}' }


@app.post("/users/items/", response_model=schema.ItemReturnSchema)
def create_item( item: schema.ItemSchema, db: Session = Depends(get_db)
):
    return crud.create_item(db=db, item=item)


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items





        


