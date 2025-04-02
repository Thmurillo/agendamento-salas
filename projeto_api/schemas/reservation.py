from pydantic import BaseModel
from datetime import time, date

class ReservationCreate(BaseModel):
    block_name: str
    room_number: int
    user_name: str
    date: date
    start_time: time
    end_time: time
    requester_course: str
    confirmation: bool
    reason: str

class ReservationSequencialCreate(BaseModel):
    block_name: str
    room_number: int
    user_name: str
    start_date: date
    end_date: date
    start_time: time
    end_time: time
    requester_course: str
    confirmation: bool
    reason: str

class ReservationResponse(BaseModel):
    id: int
    block_id: int
    room_id: int
    user_id: int
    date: date
    start_time: time
    end_time: time
    requester_course: str
    confirmation: bool
    reason: str

    class Config:
        orm_mode = True