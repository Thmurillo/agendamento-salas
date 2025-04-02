from pydantic import BaseModel
from datetime import time

class Most_Reserved_Room(BaseModel):
    room_id:int
    total:int

class Peak_hour(BaseModel):
    start_time: time
    total: int

class ReportResponse(BaseModel):
    room_mensage: str
    most_reserved_room:list[Most_Reserved_Room]
    hour_mensage: str
    peak_hour: list[Peak_hour]

