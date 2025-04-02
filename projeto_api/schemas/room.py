from pydantic import BaseModel

class RoomCreate(BaseModel):
    room_name: str | None = None
    number: int
    block_name: str
    restriction: str
    capacity: int
    resources: str | None = None

class RoomResponse(BaseModel):
    id: int
    room_name: str | None = None
    number: int
    block_id: int
    restriction: str
    capacity: int
    resources: str | None = None

    class Config:
        orm_mode = True
    
