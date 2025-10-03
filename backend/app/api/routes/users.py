from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ...db.session import get_db
from ...models.user import User
from ...schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])  # /users

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    exists = await db.scalar(select(User).where(User.email == payload.email))
    if exists:
        raise HTTPException(status_code=409, detail="Email already exists")
    user = User(name=payload.name, email=payload.email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.get("", response_model=list[UserRead])
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(User).order_by(User.id.desc()))
    return list(result)
