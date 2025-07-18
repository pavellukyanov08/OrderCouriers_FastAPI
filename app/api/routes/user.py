from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from starlette.status import HTTP_409_CONFLICT, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from app.core.database import Base, AsyncSessionLocal, get_session
from app.models.user import User
from app.schemas.user import UserCreate, Token, UserResponse
from app.core.auth import get_user, get_hashed_password, authenticate_user, create_access_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


router = APIRouter()

@router.post('/register', response_model=UserResponse)
async def register(user_data: UserCreate, db: AsyncSessionLocal = Depends(get_session)):
    existing_user =  await get_user(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Такой пользователь уже существует")

    if len(user_data.password) < 5:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Слишком короткий пароль")

    hashed_password = get_hashed_password(user_data.password)
    new_user = User(
        username=user_data.username,
        hashed_password=hashed_password
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


@router.post('/login', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSessionLocal = Depends(get_session)):
    existing_user = await authenticate_user(db, form_data.username, form_data.password)
    if not existing_user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expires = timedelta(days=1)
    access_token = create_access_token(
        data={'sub': existing_user.username},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}