""" pydantic models for the FastAPI application."""
from pydantic import BaseModel

class CalculInput(BaseModel):
    """ Pydantic model for the calculation input """
    expression: str
