"""SQLAlchemy model for the calculation table."""
from sqlalchemy import Column, Integer, String
from app.database import Base

class Calculation(Base):
    """SQLAlchemy model for the calculation table."""
    __tablename__ = "calcul"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    result = Column(String, index=True)

    def format_expression(self):
        """Return the expression in a readable format."""
        return f"Expression: {self.expression}"

    def is_valid_result(self):
        """Check if the result is a valid number."""
        try:
            float(self.result)
            return True
        except ValueError:
            return False
