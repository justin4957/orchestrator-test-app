  """
  Comprehensive test suite for Calculator power operation.
  
  This module contains unit tests, integration tests, and edge case tests
  for the calculator's power operation functionality. Tests cover basic
  functionality, type validation, error handling, and integration with
  other calculator operations.
  
  Test Categories:
      - Basic functionality tests
      - Edge case tests
      - Type validation tests
      - Boundary tests
      - Integration tests
  """
  
  import math
  import pytest
  from typing import Any, Tuple, List, Dict
  
  
  class Calculator:
      """
      Basic calculator implementation for testing purposes.
      
      This is a minimal implementation to support the test suite.
      Replace with actual Calculator import in production.
      """
      
      def power(self, base: float, exponent: float) -> float:
          """
          Raise base to the power of exponent.
          
          Args:
              base: The base number
              exponent: The exponent to raise the base to
              
          Returns:
              The result of base^exponent as a float
              
          Raises:
              ValueError: If operation results in complex number or undefined behavior
              TypeError: If inputs are not numeric types
          """
          if not isinstance(base, (int, float)) or isinstance(base, bool):
              raise TypeError(f"Base must be int or float, got {type(base).__name__}")
          if not isinstance(exponent, (int, float)) or isinstance(exponent, bool):
              raise TypeError(f"Exponent must be int or float, got {type(exponent).__name__}")
          
          if base == 0 and exponent == 0:
              raise ValueError("0^0 is mathematically undefined")
          
          if base < 0 and not float(exponent).is_integer():
              raise ValueError("Cannot raise negative number to fractional power (would result in complex number)")
          
          try:
              result = base ** exponent
              if math.isinf(result):
                  raise ValueError(f"Result overflow: {base}^{exponent} is too large")
              return float(result)
          except OverflowError:
              raise ValueError(f"Result overflow: {base}^{exponent} exceeds maximum float value")
      
      def add(self, a: float, b: float) -> float:
          """Add two numbers."""
          return float(a + b)
      
      def multiply(self, a: float, b: float) -> float:
          """Multiply two numbers."""
          return float(a * b)
  
  
  @pytest.fixture
  def calculator() -> Calculator:
      """
      Provide a fresh Calculator instance for each test.
      
      Returns:
          A new Calculator instance
      """
      return Calculator()
  
  
  @pytest.fixture
  def power_test_cases() -> List[Tuple[float, float, float]]:
      """
      Provide common test cases for power operation.
      
      Returns:
          List of tuples containing (base, exponent, expected_result)
      """
      return [
          (2, 3, 8.0),
          (5, 0, 1.0),
          (2, -2, 0.25),
          (4, 0.5, 2.0),
          (-2, 3, -8.0),
          (10, 2, 100.0),
          (3, 4, 81.0),
          (7, 1, 7.0),
      ]
  
  
  @pytest.fixture
  def edge_case_inputs() -> Dict[str, Tuple[float, float]]:
      """
      Provide edge case inputs for testing.
      
      Returns:
          Dictionary mapping edge case names to (base, exponent) tuples
      """
      return {
          'zero_zero': (0, 0),
          'negative_fractional': (-4, 0.5),
          'negative_fractional_2': (-2, 1.5),
          'large_result': (10, 308),
          'small_result': (10, -308),
      }
  
  
  class TestPowerBasicFunctionality:
      """Test basic power operation functionality."""
      
      def test_power_positive_integers(self, calculator: Calculator) -> None:
          """Test power with positive integer inputs."""
          assert calculator.power(2, 3) == 8.0
          assert calculator.power(5, 2) == 25.0
          assert calculator.power(10, 0) == 1.0
          assert calculator.power(3, 4) == 81.0
          assert calculator.power(2, 10) == 1024.0
      
      def test_power_with_floats(self, calculator: Calculator) -> None:
          """Test power with float inputs."""
          assert calculator.power(2.5, 2) == 6.25
          assert calculator.power(4.0, 0.5) == 2.0
          assert abs(calculator.power(1.5, 3) - 3.375) < 1e-10
          assert calculator.power(2.0, 3.0) == 8.0
          assert abs(calculator.power(9.0, 0.5) - 3.0) < 1e-10
      
      def test_power_negative_exponent(self, calculator: Calculator) -> None:
          """Test power with negative exponents."""
          assert calculator.power(2, -2) == 0.25
          assert calculator.power(10, -1) == 0.1
          assert calculator.power(5, -3) == 0.008
          assert calculator.power(4, -1) == 0.25
          assert abs(calculator.power(2, -3) - 0.125) < 1e-10
      
      def test_power_zero_exponent(self, calculator: Calculator) -> None:
          """Test any number to power of 0 equals 1."""
          assert calculator.power(5, 0) == 1.0
          assert calculator.power(100, 0) == 1.0
          assert calculator.power(-5, 0) == 1.0
          assert calculator.power(0.5, 0) == 1.0
          assert calculator.power(1000000, 0) == 1.0
      
      def test_power_zero_base(self, calculator: Calculator) -> None:
          """Test zero raised to positive powers."""
          assert calculator.power(0, 5) == 0.0
          assert calculator.power(0, 1) == 0.0
          assert calculator.power(0, 100) == 0.0
          assert calculator.power(0, 0.5) == 0.0
          assert calculator.power(0, 2.5) == 0.0
      
      def test_power_returns_float(self, calculator: Calculator) -> None:
          """Test that power always returns float type."""
          result = calculator.power(2, 3)
          assert isinstance(result, float)
          
          result = calculator.power(5, 0)
          assert isinstance(result, float)
          
          result = calculator.power(4, 2)
          assert isinstance(result, float)
      
      def test_power_parametrized(self, calculator: Calculator, power_test_cases: List[Tuple[float, float, float]]) -> None:
          """Test power with parametrized test cases."""
          for base, exponent, expected in power_test_cases:
              result = calculator.power(base, exponent)
              assert abs(result - expected) < 1e-10, f"Failed for {base}^{exponent}"
  
  
  class TestPowerEdgeCases:
      """Test edge cases for power operation."""
      
      def test_power_zero_to_zero(self, calculator: Calculator) -> None:
          """Test 0^0 raises ValueError."""
          with pytest.raises(ValueError, match="0\\^0 is mathematically undefined"):
              calculator.power(0, 0)
      
      def test_power_negative_base_fractional_exponent(self, calculator: Calculator) -> None:
          """Test negative base with fractional exponent raises ValueError."""
          with pytest.raises(ValueError, match="Cannot raise negative number to fractional power"):
              calculator.power(-4, 0.5)
          
          with pytest.raises(ValueError, match="Cannot raise negative number to fractional power"):
              calculator.power(-2, 1.5)
          
          with pytest.raises(ValueError, match="Cannot raise negative number to fractional power"):
              calculator.power(-10, 0.25)
      
      def test_power_negative_base_integer_exponent(self, calculator: Calculator) -> None:
          """Test negative base with integer exponent works correctly."""
          assert calculator.power(-2, 3) == -8.0
          assert calculator.power(-2, 2) == 4.0
          assert calculator.power(-3, 4) == 81.0
          assert calculator.power(-1, 5) == -1.0
          assert calculator.power(-5, 2) == 25.0
      
      def test_power_large_numbers(self, calculator: Calculator) -> None:
          """Test power with very large results."""
          result = calculator.power(10, 100)
          assert result == 1e100
          
          result = calculator.power(2, 100)
          assert result > 0
          
          with pytest.raises(ValueError, match="Result overflow"):
              calculator.power(10, 309)
      
      def test_power_very_small_results(self, calculator: Calculator) -> None:
          """Test power resulting in very small numbers."""
          result = calculator.power(10, -100)
          assert result == 1e-100
          
          result = calculator.power(2, -50)
          assert result > 0
          assert result < 1e-10
      
      def test_power_fractional_base_negative_exponent(self, calculator: Calculator) -> None:
          """Test fractional base with negative exponent."""
          assert calculator.power(0.5, -1) == 2.0
          assert calculator.power(0.25, -2) == 16.0
          assert abs(calculator.power(0.1, -1) - 10.0) < 1e-10
  
  
  class TestPowerTypeValidation:
      """Test type validation for power operation."""
      
      def test_power_invalid_base_type_string(self, calculator: Calculator) -> None:
          """Test TypeError raised for string base."""
          with pytest.raises(TypeError, match="Base must be int or float, got str"):
              calculator.power("2", 3)
      
      def test_power_invalid_base_type_none(self, calculator: Calculator) -> None:
          """Test TypeError raised for None base."""
          with pytest.raises(TypeError, match="Base must be int or float, got NoneType"):
              calculator.power(None, 3)
      
      def test_power_invalid_base_type_list(self, calculator: Calculator) -> None:
          """Test TypeError raised for list base."""
          with pytest.raises(TypeError, match="Base must be int or float, got list"):
              calculator.power([2], 3)
      
      def test_power_invalid_base_type_dict(self, calculator: Calculator) -> None:
          """Test TypeError raised for dict base."""
          with pytest.raises(TypeError, match="Base must be int or float, got dict"):
              calculator.power({"value": 2}, 3)
      
      def test_power_invalid_exponent_type_string(self, calculator: Calculator) -> None:
          """Test TypeError raised for string exponent."""
          with pytest.raises(TypeError, match="Exponent must be int or float, got str"):
              calculator.power(2, "3")
      
      def test_power_invalid_exponent_type_none(self, calculator: Calculator) -> None:
          """Test TypeError raised for None exponent."""
          with pytest.raises(TypeError, match="Exponent must be int or float, got NoneType"):
              calculator.power(2, None)
      
      def test_power_invalid_exponent_type_list(self, calculator: Calculator) -> None:
          """Test TypeError raised for list exponent."""
          with pytest.raises(TypeError, match="Exponent must be int or float, got list"):
              calculator.power(2, [3])
      
      def test_power_invalid_exponent_type_dict(self, calculator: Calculator) -> None:
          """Test TypeError raised for dict exponent."""
          with pytest.raises(TypeError, match="Exponent must be int or float, got dict"):
              calculator.power(2, {"value": 3})
      
      def test_power_boolean_base(self, calculator: Calculator) -> None:
          """Test that boolean base is rejected."""
          with pytest.raises(TypeError, match="Base must be int or float, got bool"):
              calculator.power(True, 3)
          
          with pytest.raises(TypeError, match="Base must be int or float, got bool"):
              calculator.power(False, 3)
      
      def test_power_boolean_exponent(self, calculator: Calculator) -> None:
          """Test that boolean exponent is rejected."""
          with pytest.raises(TypeError, match="Exponent must be int or float, got bool"):
              calculator.power(2, True)
          
          with pytest.raises(TypeError, match="Exponent must be int or float, got bool"):
              calculator.power(2, False)
  
  
  class TestPowerBoundaryConditions:
      """Test boundary conditions for power operation."""
      
      def test_power_fractional_results(self, calculator: Calculator) -> None:
          """Test power operations resulting in fractions."""
          assert calculator.power(4, 0.5) == 2.0
          assert abs(calculator.power(27, 1/3) - 3.0) < 1e-10
          assert calculator.power(16, 0.25) == 2.0
          assert abs(calculator.power(8, 1/3) - 2.0) < 1e-10
      
      def test_power_one_as_base(self, calculator: Calculator) -> None:
          """Test 1 raised to any power equals 1."""
          assert calculator.power(1, 100) == 1.0
          assert calculator.power(1, -5) == 1.0
          assert calculator.power(1, 0) == 1.0
          assert calculator.power(1, 0.5) == 1.0
          assert calculator.power(1, -100) == 1.0
      
      def test_power_one_as_exponent(self, calculator: Calculator) -> None:
          """Test any number raised to 1 equals itself."""
          assert calculator.power(5, 1) == 5.0
          assert calculator.power(-3, 1) == -3.0
          assert calculator.power(2.5, 1) == 2.5
          assert calculator.power(0, 1) == 0.0
          assert calculator.power(1000, 1) == 1000.0
      
      def test_power_negative_one_base(self, calculator: Calculator) -> None:
          """Test -1 raised to various powers."""
          assert calculator.power(-1, 2) == 1.0
          assert calculator.power(-1, 3) == -1.0
          assert calculator.power(-1, 4) == 1.0
          assert calculator.power(-1, 0) == 1.0
      
      def test_power_very_small_base(self, calculator: Calculator) -> None:
          """Test very small base values."""
          result = calculator.power(0.001, 2)
          assert abs(result - 0.000001) < 1e-15
          
          result = calculator.power(0.1, 10)
          assert abs(result - 1e-10) < 1e-20
      
      def test_power_mixed_signs(self, calculator: Calculator) -> None:
          """Test power with mixed positive/negative values."""
          assert calculator.power(-2, -2) == 0.25
          assert calculator.power(2, -3) == 0.125
          assert calculator.power(-3, -2) == 1/9
  
  
  class TestPowerIntegration:
      """Test integration of power operation with other calculator methods."""
      
      def test_power_with_add(self, calculator: Calculator) -> None:
          """Test power operation combined with addition."""
          power_result = calculator.power(2, 3)
          result = calculator.add(power_result, 5)
          assert result == 13.0
          
          result = calculator.add(calculator.power(3, 2), calculator.power(4,