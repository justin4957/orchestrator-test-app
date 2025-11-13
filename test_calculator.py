"""Tests for calculator module."""

import pytest
import math
from calculator import Calculator


def test_add():
    """Test addition."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract():
    """Test subtraction."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(0, 5) == -5


def test_multiply():
    """Test multiplication."""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 100) == 0


def test_divide():
    """Test division."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5


def test_divide_by_zero():
    """Test division by zero raises error."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


def test_power_positive_integers():
    """Test power with positive integer inputs."""
    calc = Calculator()
    assert calc.power(2, 3) == 8.0
    assert calc.power(5, 2) == 25.0
    assert calc.power(10, 0) == 1.0
    assert calc.power(3, 4) == 81.0


def test_power_with_floats():
    """Test power with float inputs."""
    calc = Calculator()
    assert calc.power(2.5, 2) == 6.25
    assert calc.power(4.0, 0.5) == 2.0
    assert calc.power(1.5, 3) == 3.375
    assert calc.power(9.0, 0.5) == 3.0


def test_power_negative_exponent():
    """Test power with negative exponents."""
    calc = Calculator()
    assert calc.power(2, -2) == 0.25
    assert calc.power(10, -1) == 0.1
    assert calc.power(5, -3) == 0.008
    assert calc.power(4, -0.5) == 0.5


def test_power_zero_exponent():
    """Test any number to power of 0 equals 1."""
    calc = Calculator()
    assert calc.power(5, 0) == 1.0
    assert calc.power(100, 0) == 1.0
    assert calc.power(-5, 0) == 1.0
    assert calc.power(0.5, 0) == 1.0


def test_power_zero_base():
    """Test zero raised to positive powers."""
    calc = Calculator()
    assert calc.power(0, 5) == 0.0
    assert calc.power(0, 1) == 0.0
    assert calc.power(0, 100) == 0.0
    assert calc.power(0, 0.5) == 0.0


def test_power_zero_to_zero():
    """Test 0^0 raises ValueError."""
    calc = Calculator()
    with pytest.raises(ValueError, match="0\\^0 is mathematically undefined"):
        calc.power(0, 0)


def test_power_negative_base_fractional_exponent():
    """Test negative base with fractional exponent raises ValueError."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot raise negative number to fractional power"):
        calc.power(-4, 0.5)
    with pytest.raises(ValueError, match="Cannot raise negative number to fractional power"):
        calc.power(-2, 1.5)
    with pytest.raises(ValueError, match="Cannot raise negative number to fractional power"):
        calc.power(-8, 0.333)


def test_power_negative_base_integer_exponent():
    """Test negative base with integer exponent works correctly."""
    calc = Calculator()
    assert calc.power(-2, 3) == -8.0
    assert calc.power(-2, 2) == 4.0
    assert calc.power(-3, 4) == 81.0
    assert calc.power(-5, 3) == -125.0


def test_power_large_numbers():
    """Test power with very large results."""
    calc = Calculator()
    result = calc.power(10, 100)
    assert result == 1e100
    
    with pytest.raises(ValueError, match="Result overflow"):
        calc.power(10, 309)
    
    with pytest.raises(ValueError, match="Result overflow"):
        calc.power(2, 10000)


def test_power_very_small_results():
    """Test power resulting in very small numbers."""
    calc = Calculator()
    result = calc.power(10, -100)
    assert result == 1e-100
    
    result = calc.power(2, -50)
    assert result > 0
    assert result < 1e-10


def test_power_invalid_base_type():
    """Test TypeError raised for invalid base type."""
    calc = Calculator()
    
    with pytest.raises(TypeError, match="Base must be int or float"):
        calc.power("2", 3)
    
    with pytest.raises(TypeError, match="Base must be int or float"):
        calc.power(None, 3)
    
    with pytest.raises(TypeError, match="Base must be int or float"):
        calc.power([2], 3)
    
    with pytest.raises(TypeError, match="Base must be int or float"):
        calc.power({"base": 2}, 3)


def test_power_invalid_exponent_type():
    """Test TypeError raised for invalid exponent type."""
    calc = Calculator()
    
    with pytest.raises(TypeError, match="Exponent must be int or float"):
        calc.power(2, "3")
    
    with pytest.raises(TypeError, match="Exponent must be int or float"):
        calc.power(2, None)
    
    with pytest.raises(TypeError, match="Exponent must be int or float"):
        calc.power(2, [3])
    
    with pytest.raises(TypeError, match="Exponent must be int or float"):
        calc.power(2, {"exp": 3})


def test_power_boolean_inputs():
    """Test that boolean inputs are rejected despite being numeric."""
    calc = Calculator()
    
    with pytest.raises(TypeError, match="Base must be int or float"):
        calc.power(True, 3)
    
    with pytest.raises(TypeError, match="Base must be int or float"):
        calc.power(False, 3)
    
    with pytest.raises(TypeError, match="Exponent must be int or float"):
        calc.power(2, True)
    
    with pytest.raises(TypeError, match="Exponent must be int or float"):
        calc.power(2, False)


def test_power_fractional_results():
    """Test power operations resulting in fractions."""
    calc = Calculator()
    assert calc.power(4, 0.5) == 2.0
    assert abs(calc.power(27, 1/3) - 3.0) < 0.0001
    assert calc.power(16, 0.25) == 2.0
    assert calc.power(8, 1/3) == pytest.approx(2.0, rel=1e-9)


def test_power_one_as_base():
    """Test 1 raised to any power equals 1."""
    calc = Calculator()
    assert calc.power(1, 100) == 1.0
    assert calc.power(1, -5) == 1.0
    assert calc.power(1, 0) == 1.0
    assert calc.power(1, 0.5) == 1.0


def test_power_one_as_exponent():
    """Test any number raised to 1 equals itself."""
    calc = Calculator()
    assert calc.power(5, 1) == 5.0
    assert calc.power(-3, 1) == -3.0
    assert calc.power(2.5, 1) == 2.5


def test_power_with_other_operations():
    """Test power operation combined with add, subtract, multiply, divide."""
    calc = Calculator()
    
    power_result = calc.power(2, 3)
    assert calc.add(power_result, 5) == 13.0
    
    power_result = calc.power(2, 2)
    assert calc.multiply(power_result, 3) == 12.0
    
    power_result = calc.power(10, 2)
    assert calc.subtract(power_result, 50) == 50.0
    
    power_result = calc.power(4, 2)
    assert calc.divide(power_result, 4) == 4.0


def test_power_return_type():
    """Test that power always returns float type."""
    calc = Calculator()
    
    result = calc.power(2, 3)
    assert isinstance(result, float)
    
    result = calc.power(5, 0)
    assert isinstance(result, float)
    
    result = calc.power(10, -2)
    assert isinstance(result, float)


@pytest.fixture
def calculator():
    """Provide a fresh Calculator instance for each test."""
    return Calculator()


@pytest.fixture
def power_test_cases():
    """Provide common test cases for power operation."""
    return [
        (2, 3, 8.0),
        (5, 0, 1.0),
        (2, -2, 0.25),
        (4, 0.5, 2.0),
        (-2, 3, -8.0),
        (10, 2, 100.0),
    ]


@pytest.fixture
def edge_case_inputs():
    """Provide edge case inputs for testing."""
    return {
        'zero_zero': (0, 0),
        'negative_fractional': (-4, 0.5),
        'large_result': (10, 308),
        'small_result': (10, -308),
    }


def test_power_with_fixtures(calculator, power_test_cases):
    """Test power operation using fixtures."""
    for base, exponent, expected in power_test_cases:
        result = calculator.power(base, exponent)
        assert result == expected


def test_power_edge_cases_with_fixtures(calculator, edge_case_inputs):
    """Test edge cases using fixtures."""
    with pytest.raises(ValueError):
        calculator.power(*edge_case_inputs['zero_zero'])
    
    with pytest.raises(ValueError):
        calculator.power(*edge_case_inputs['negative_fractional'])
    
    with pytest.raises(ValueError):
        calculator.power(*edge_case_inputs['large_result'])