from sqlalchemy.orm import Session
from app.models import Calculation
from app.database import SessionLocal

async def saveCalculation(expression: str, result: str):
    session = SessionLocal()
    calc = Calculation(expression=expression, result=result)
    session.add(calc)
    session.commit()
    session.close()

async def getCalculations():
    session = SessionLocal()
    calculations = session.query(Calculation).all()
    session.close()
    return calculations