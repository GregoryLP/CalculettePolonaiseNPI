"""Defines the routes for the calculation API."""
import csv
import io
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.shemas import CalculInput
from app.crud import save_calculation, getcalculations
from app.utils import evaluate_npi


router = APIRouter()

@router.post("/calculate")
async def calculate(calculation_input = CalculInput):
    """Calculate the result of an expression"""
    try:
        result = evaluate_npi(calculation_input.expression)
        await save_calculation(calculation_input.expression, result)
        return {"expression": calculation_input.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {e}") from e

@router.get("/exportCalcul")
async def export_calcul():
    """Export all calculations to a CSV file"""
    calculations = await getcalculations()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["expression", "result"])

    for calculation in calculations:
        writer.writerow([calculation.expression, calculation.result])

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=calcul.csv"})
