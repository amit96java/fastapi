from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

#dto
#BaseModel is coming from pydantic lib
# model for schema declaration and also work as dto
#here BaseModel is extending

class PostBase(BaseModel):
    id: int
    title:str
    content:str
    published:int = 1


class PostCreate(PostBase):
    # owner_id:int
    pass


class UserCreate(BaseModel):
    id:int
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    class Config: #to convert orm to pydantic dto
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type:str
    class Config: #to convert orm to pydantic dto
        orm_mode = True

class TokenData(BaseModel):
    id:Optional[str] = None

class Post(BaseModel):
    title:str
    # content:str
    # published:int
    owner_id:int
    owner:UserResponse
    class Config: #to convert orm to pydantic dto
        orm_mode = True

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)