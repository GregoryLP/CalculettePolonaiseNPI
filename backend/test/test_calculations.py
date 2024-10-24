import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils import evaluate_npi

client = TestClient(app)

# Test evaluate npi
def testEvaluateaddition():
    expression = "3 5 +"
    result = evaluate_npi(expression)
    assert result == 8

def testEvalutateSubtraction():
    expression = "3 5 -"
    result = evaluate_npi(expression)
    assert result == -2

def testEvaluateMultiplication():
    expression = "3 5 *"
    result = evaluate_npi(expression)
    assert result == 15

def testEvaluateDivision():
    expression = "3 5 /"
    result = evaluate_npi(expression)
    assert result == 0.6

def testEvaluateExpressionNegativeNumber():
    expression = "3 -5 +"
    result = evaluate_npi(expression)
    assert result == -2
def testEvaluateInvalidExpression():
    expression = "3 5 6 +"
    with pytest.raises(ValueError, match="The user input has too many values or not enough values to produce a single result."):
        result = evaluate_npi(expression)

def testEvaluateInvalidExpressionOperator():
    expression = "3 6 ?"
    with pytest.raises(ValueError, match="Invalid token: ?"):
        result = evaluate_npi(expression)

def testEvaluateInvalidExpressionNoSpace():
    expression = "35 +"
    with pytest.raises(ValueError, match="Not enough values in stack for operation"):
        result = evaluate_npi(expression)

def testEvaluateInvalidExpressionNoPlaceEnd():
    expression = "3 + 6 5"
    with pytest.raises(ValueError, match="Not enough values in stack for operation"):
        result = evaluate_npi(expression)