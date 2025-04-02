from pydantic import BaseModel

class BlockCreate(BaseModel):
    block_name: str

class BlockResponse(BaseModel):
    id: int
    block_name: str

    class Config:
        orm_mode = True


