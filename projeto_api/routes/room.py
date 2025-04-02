from fastapi import APIRouter, Depends, status, HTTPException
from schemas.room import RoomCreate, RoomResponse
from models.room import Room
from models.block import Block
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_session

router = APIRouter()

@router.post("/room", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
async def create_room(room: RoomCreate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Block).where(Block.block_name == room.block_name))
    block = result.scalars().first()

    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    
    new_room = Room(
        room_name=room.room_name,
        number=room.number,
        block_id=block.id,
        restriction = room.restriction,
        capacity=room.capacity,
        resources=room.resources
    )

    session.add(new_room)
    await session.commit()
    await session.refresh(new_room)

    return new_room

@router.get("/room", response_model=list[RoomResponse], status_code=status.HTTP_200_OK)
async def get_room(session: AsyncSession= Depends(get_session)):
    result = await session.execute(select(Room))
    room = result.scalars().all()

    return room

@router.get("/room/{room_id}", response_model=RoomResponse, status_code=status.HTTP_200_OK)
async def get_room_by_id(room_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Room).where(Room.id == room_id))
    room = result.scalars().first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    return room

@router.put("/room/{room_id}", response_model=RoomResponse, status_code=status.HTTP_200_OK)
async def update_room(room_id: int, updated_room: RoomCreate, session: AsyncSession = Depends(get_session)):
    room_result = await session.execute(select(Room).where(Room.id == room_id))
    room = room_result.scalars().first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    block_result = await session.execute(select(Block).where(Block.block_name == updated_room.block_name))
    block = block_result.scalars().first()

    if not block:
        raise HTTPException(status_code=404, detail="Block not found")

    room.room_name = updated_room.room_name
    room.number = updated_room.number
    room.block_id = block.id 
    room.restriction = updated_room.restriction 
    room.capacity = updated_room.capacity
    room.resources = updated_room.resources

    await session.commit()
    await session.refresh(room)

    return room

@router.delete("/room/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_room(room_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Room).where(Room.id == room_id))
    room = result.scalars().first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    await session.delete(room)
    await session.commit()



