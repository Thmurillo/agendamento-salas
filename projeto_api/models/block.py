from .base import Base
from sqlalchemy import String, Column, Integer

class Block(Base):
    __tablename__ = "blocks"

    id = Column(Integer, primary_key = True)
    block_name = Column(String, nullable = False)
