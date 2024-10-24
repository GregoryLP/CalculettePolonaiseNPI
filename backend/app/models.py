from sqlalchemy import Column, Integer, String
from database import Base

class Calculation(Base):
    __tablename__ = "calcul"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    result = Column(String, index=True)