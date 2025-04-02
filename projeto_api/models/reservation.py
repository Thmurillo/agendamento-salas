from .base import Base
from sqlalchemy import String, Integer, Column, ForeignKey, Time, Boolean, Date

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key = True)
    block_id = Column(Integer, ForeignKey("blocks.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable = False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable = False)
    end_time = Column(Time, nullable = False)
    requester_course = Column(String, nullable= False)
    confirmation = Column(Boolean, nullable = False)
    reason = Column(String, nullable = False)