""" This file contains the tests for the calculations module. """
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils import evaluate_npi

client = TestClient(app)

# Test evaluate npi
def test_evaluate_addition():
    """Test evaluate_npi function with addition."""
    expression = "3 5 +"
    result = evaluate_npi(expression)
    assert result == 8

def test_evalutate_subtraction():
    """Test evaluate_npi function with subtraction."""
    expression = "3 5 -"
    result = evaluate_npi(expression)
    assert result == -2

def test_evaluate_multiplication():
    """Test evaluate_npi function with multiplication."""
    expression = "3 5 *"
    result = evaluate_npi(expression)
    assert result == 15

def test_evaluate_division():
    """Test evaluate_npi function with division."""
    expression = "3 5 /"
    result = evaluate_npi(expression)
    assert result == 0.6

def test_evaluate_expression_negative_number():
    """Test evaluate_npi function with negative number."""
    expression = "3 -5 +"
    result = evaluate_npi(expression)
    assert result == -2
def test_evaluate_invalid_expression():
    """Test evaluate_npi function with invalid expression."""
    expression = "3 5 6 +"
    with pytest.raises(ValueError, match="The input has too many values"
                        + "or not enough values to produce a result."):
        evaluate_npi(expression)

def test_evaluate_invalid_expression_operator():
    """Test evaluate_npi function with invalid operator."""
    expression = "3 6 ?"
    with pytest.raises(ValueError, match="Invalid token: ?"):
        evaluate_npi(expression)

def test_evaluate_invalid_expression_no_space():
    """Test evaluate_npi function with no space between values and operator."""
    expression = "35 +"
    with pytest.raises(ValueError, match="Not enough values in stack for operation"):
        evaluate_npi(expression)

def test_evaluate_invalid_expression_no_place_end():
    """Test evaluate_npi function with no space between values and operator."""
    expression = "10 5 + 3 *"
    with pytest.raises(ValueError, match="Not enough values in stack for operation"):
        evaluate_npi(expression)
