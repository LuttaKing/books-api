from sqlalchemy.orm import Session

import models, schema


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    db_user=get_user(db,user_id)
    if db_user is not None:
        db.delete(db_user)
        db.commit()
        return db_user
    else:
        return None
    
def update_user(db: Session, user:  schema.UserSchema):
    db_user=get_user(db,user.id)
    if db_user is not None:
    
        for key, value in user.dict().items():
            setattr(db_user, key, value) if value else None
        
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserSchema):
    db_user = models.User(email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schema.ItemSchema):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
