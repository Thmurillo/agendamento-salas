from .base import Base
from sqlalchemy import String, Integer, Column

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable=False)
    login = Column(String, nullable = False)
    user_password = Column(String, nullable = False)
    user_type = Column(String, nullable = False)