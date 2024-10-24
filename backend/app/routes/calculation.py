from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from shemas import CalculInput
from crud import saveCalculation, getCalculations
from utils import evaluate_npi
import csv
import io

router = APIRouter()

@router.post("/calculate")
async def calculate(input: CalculInput):
    try: 
        result = evaluate_npi(input.expression)
        await saveCalculation(input.expression, result)
        return {"expression": input.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {e}")
    
@router.get("/exportCalcul")
async def exportCalcul():
    calculations = await getCalculations()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["expression", "result"])

    for calculation in calculations:
        writer.writerow([calculation.expression, calculation.result])

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=calcul.csv"})