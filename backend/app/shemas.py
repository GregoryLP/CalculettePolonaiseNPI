from pydantic import BaseModel

class CalculInput(BaseModel):
    expression: str