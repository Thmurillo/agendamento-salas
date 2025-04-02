from .base import Base
from sqlalchemy import String, Column, Integer, ForeignKey

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key = True)
    room_name = Column(String, nullable = True)
    number = Column(Integer, nullable = False)
    block_id = Column(Integer, ForeignKey("blocks.id"), nullable = False)
    restriction = Column(String, nullable= False)
    capacity = Column(Integer, nullable = False)
    resources = Column(String, nullable = True)
