from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from starlette.status import HTTP_409_CONFLICT

from app.core.database import Base, AsyncSessionLocal, get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post('/register', response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSessionLocal = Depends(get_session)):
    # user = select(User).where(User.username == user.username)
    result = await db.execute(user)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Имя пользователя занято")

    # new_user = User(
    #     email=user.email,
    #     username=user.username,
    #     hashed_password=user=user.hashed_password
    #
    # )

