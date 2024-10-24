""" CRUD operations for the app """
from app.models import Calculation
from app.database import SessionLocal

async def save_calculation(expression: str, result: str):
    """ Save calculation to the database """
    session = SessionLocal()
    calc = Calculation(expression=expression, result=result)
    session.add(calc)
    session.commit()
    session.close()

async def getcalculations():
    """ Retrieve all calculations from the database """
    session = SessionLocal()
    calculations = session.query(Calculation).all()
    session.close()
    return calculations
