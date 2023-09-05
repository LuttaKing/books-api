from pydantic import BaseModel,field_validator


class ItemSchema(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str | None = None

    @field_validator('title')
    def title_must_be_caps(cls,value):
        if not value.isupper():
            raise ValueError('title must be upper case')
        return value


    class Config:
        from_attributes = True

# just schema for return item
class ItemReturnSchema(BaseModel):
    title: str
    description: str | None = None

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    id: int | None
    email: str
    hashed_password: str
    is_active: bool
    items: list[ItemSchema] | None = []

    class Config:
        from_attributes = True
