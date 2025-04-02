from fastapi import APIRouter, Depends, status, HTTPException
from schemas.user import UserCreate, UserResponse
from models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_session

router = APIRouter()

@router.post("/user", response_model = UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    new_user = User(
        user_name = user.user_name,
        login = user.login,
        user_password = user.user_password,
        user_type = user.user_type
    )

    session.add(new_user)

    await session.commit()
    await session.refresh(new_user)

    print("Novo usuario:", new_user)

    return new_user

@router.get("/user", response_model = list[UserResponse], status_code=status.HTTP_200_OK)
async def get_user(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users

@router.get("/user/{user_id}", response_model = UserResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    
    return user

@router.put("/user/{user_id}", response_model= UserResponse, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, update_user: UserCreate, session: AsyncSession= Depends(get_session)):
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code =404, detail= "User not found")
    
    user.user_name = update_user.user_name
    user.login = update_user.login
    user.user_password = update_user.user_password
    user.user_type = update_user.user_type

    await session.commit()
    await session.refresh(user)

    return user

@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_users(user_id:int, session: AsyncSession= Depends(get_session)):
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code =404, detail= "User not found")

    await session.delete(user)
    await session.commit()


