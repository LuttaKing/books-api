from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str | None = None

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    id: int
    email: str
    hashed_password: str
    is_active: bool
    items: list[ItemSchema] = []

    class Config:
        orm_mode = True
