from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserRead(BaseModel):
    id: int
    email: Optional[EmailStr]
    username: str

    model_config = {'from_attributes': True}


class UserCreate(BaseModel):
    email: Optional[EmailStr] = None
    password: str = Field(min_length=3)
    username: str = Field(min_length=3)


class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    username: str

    model_config = {
        'from_attributes': True
    }


