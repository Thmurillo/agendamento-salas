from fastapi import APIRouter, Depends, status, HTTPException
from schemas.block import BlockCreate, BlockResponse
from models.block import Block
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_session

router = APIRouter()

@router.post("/block", response_model= BlockResponse, status_code=status.HTTP_201_CREATED)
async def create_block(block: BlockCreate, session: AsyncSession = Depends(get_session)):
    new_block = Block(
        block_name = block.block_name
    )

    session.add(new_block)

    await session.commit()
    await session.refresh(new_block)

    return new_block

@router.get("/block", response_model= list[BlockResponse], status_code=status.HTTP_200_OK)
async def get_block(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Block))
    block = result.scalars().all()

    return block

@router.get("/block/{block_id}", response_model= BlockResponse, status_code=status.HTTP_200_OK)
async def get_block_by_id(block_id: int,session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Block).where(Block.id == block_id))
    block = result.scalars().first()

    if not block:
        raise HTTPException(status_code=404, detail="User not found")

    return block

@router.put("/block/{block_id}", response_model= BlockResponse, status_code=status.HTTP_200_OK)
async def update_block(block_id:int, block_update:BlockCreate, session: AsyncSession= Depends(get_session)):
    result = await session.execute(select(Block).where(Block.id == block_id))
    block = result.scalars().first()

    if not block:
        raise HTTPException(status_code=404, detail="User not found")
    
    block.block_name = block_update.block_name

    await session.commit()
    await session.refresh(block)

    return block

@router.delete("/block/{block_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_block(block_id:int, session: AsyncSession= Depends(get_session)):
    result = await session.execute(select(Block).where(Block.id == block_id))
    block = result.scalars().first()

    if not block:
        raise HTTPException(status_code=404, detail="User not found")
    
    await session.delete(block)
    await session.commit()

