from .base import Base
from sqlalchemy import String, Integer, Column, ForeignKey

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True)
    user_id =Column(Integer, ForeignKey("users.id"), nullable = False)
    full_name =Column(String, nullable= False)
    cpf = Column(String, nullable= False)
    academic_registry = Column(String, nullable= False)
    email = Column(String, nullable= False)
    course = Column(String, nullable= False)