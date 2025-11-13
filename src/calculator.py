  """
  Calculator Module
  
  A production-ready calculator implementation with support for basic arithmetic
  operations including addition, subtraction, multiplication, division, and
  power operations.
  
  This module provides a Calculator class that performs mathematical operations
  with comprehensive error handling, type validation, and edge case management.
  
  Example:
      >>> calc = Calculator()
      >>> calc.add(5, 3)
      8.0
      >>> calc.power(2, 3)
      8.0
      >>> calc.divide(10, 2)
      5.0
  """
  
  import math
  from typing import Union
  
  
  class Calculator:
      """
      A calculator class that provides basic arithmetic operations.
      
      This class implements standard mathematical operations with robust error
      handling and type validation. All operations return float values for
      consistency.
      
      Attributes:
          None
      
      Example:
          >>> calc = Calculator()
          >>> calc.add(10, 5)
          15.0
          >>> calc.power(2, 8)
          256.0
      """
      
      def add(self, a: Union[int, float], b: Union[int, float]) -> float:
          """
          Add two numbers together.
          
          Args:
              a: The first number to add
              b: The second number to add
          
          Returns:
              The sum of a and b as a float
          
          Raises:
              TypeError: If inputs are not numeric types
          
          Examples:
              >>> calc = Calculator()
              >>> calc.add(5, 3)
              8.0
              >>> calc.add(2.5, 1.5)
              4.0
              >>> calc.add(-5, 10)
              5.0
          """
          if not isinstance(a, (int, float)) or isinstance(a, bool):
              raise TypeError(f"First argument must be int or float, got {type(a).__name__}")
          if not isinstance(b, (int, float)) or isinstance(b, bool):
              raise TypeError(f"Second argument must be int or float, got {type(b).__name__}")
          
          return float(a + b)
      
      def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
          """
          Subtract the second number from the first.
          
          Args:
              a: The number to subtract from
              b: The number to subtract
          
          Returns:
              The difference of a and b as a float
          
          Raises:
              TypeError: If inputs are not numeric types
          
          Examples:
              >>> calc = Calculator()
              >>> calc.subtract(10, 3)
              7.0
              >>> calc.subtract(5.5, 2.5)
              3.0
              >>> calc.subtract(3, 8)
              -5.0
          """
          if not isinstance(a, (int, float)) or isinstance(a, bool):
              raise TypeError(f"First argument must be int or float, got {type(a).__name__}")
          if not isinstance(b, (int, float)) or isinstance(b, bool):
              raise TypeError(f"Second argument must be int or float, got {type(b).__name__}")
          
          return float(a - b)
      
      def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
          """
          Multiply two numbers together.
          
          Args:
              a: The first number to multiply
              b: The second number to multiply
          
          Returns:
              The product of a and b as a float
          
          Raises:
              TypeError: If inputs are not numeric types
          
          Examples:
              >>> calc = Calculator()
              >>> calc.multiply(5, 3)
              15.0
              >>> calc.multiply(2.5, 4)
              10.0
              >>> calc.multiply(-3, 7)
              -21.0
          """
          if not isinstance(a, (int, float)) or isinstance(a, bool):
              raise TypeError(f"First argument must be int or float, got {type(a).__name__}")
          if not isinstance(b, (int, float)) or isinstance(b, bool):
              raise TypeError(f"Second argument must be int or float, got {type(b).__name__}")
          
          return float(a * b)
      
      def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
          """
          Divide the first number by the second.
          
          Args:
              a: The dividend (number to be divided)
              b: The divisor (number to divide by)
          
          Returns:
              The quotient of a divided by b as a float
          
          Raises:
              TypeError: If inputs are not numeric types
              ValueError: If attempting to divide by zero
          
          Examples:
              >>> calc = Calculator()
              >>> calc.divide(10, 2)
              5.0
              >>> calc.divide(7, 2)
              3.5
              >>> calc.divide(15, 3)
              5.0
          """
          if not isinstance(a, (int, float)) or isinstance(a, bool):
              raise TypeError(f"First argument must be int or float, got {type(a).__name__}")
          if not isinstance(b, (int, float)) or isinstance(b, bool):
              raise TypeError(f"Second argument must be int or float, got {type(b).__name__}")
          
          if b == 0:
              raise ValueError("Cannot divide by zero")
          
          return float(a / b)
      
      def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
          """
          Raise base to the power of exponent.
          
          This method computes base^exponent with comprehensive error handling
          for edge cases including negative bases with fractional exponents,
          the undefined 0^0 case, and overflow scenarios.
          
          Args:
              base: The base number to be raised to a power
              exponent: The exponent to raise the base to
          
          Returns:
              The result of base^exponent as a float
          
          Raises:
              TypeError: If inputs are not numeric types (int or float)
              ValueError: If operation results in complex number (negative base
                  with fractional exponent), undefined behavior (0^0), or
                  overflow (result too large to represent)
          
          Examples:
              >>> calc = Calculator()
              >>> calc.power(2, 3)
              8.0
              >>> calc.power(5, 0)
              1.0
              >>> calc.power(2, -2)
              0.25
              >>> calc.power(4, 0.5)
              2.0
              >>> calc.power(-2, 3)
              -8.0
              >>> calc.power(10, 2)
              100.0
          
          Notes:
              - Any number (except 0) raised to power 0 equals 1
              - Negative exponents return fractional results
              - Negative base with integer exponent is supported
              - Negative base with fractional exponent raises ValueError
              - 0^0 is mathematically undefined and raises ValueError
          """
          if not isinstance(base, (int, float)) or isinstance(base, bool):
              raise TypeError(f"Base must be int or float, got {type(base).__name__}")
          if not isinstance(exponent, (int, float)) or isinstance(exponent, bool):
              raise TypeError(f"Exponent must be int or float, got {type(exponent).__name__}")
          
          if base == 0 and exponent == 0:
              raise ValueError("0^0 is mathematically undefined")
          
          if base < 0 and not float(exponent).is_integer():
              raise ValueError(
                  f"Cannot raise negative number to fractional power: "
                  f"{base}^{exponent} would result in complex number"
              )
          
          try:
              result = base ** exponent
              
              if math.isinf(result):
                  raise ValueError(
                      f"Result overflow: {base}^{exponent} is too large to represent"
                  )
              
              return float(result)
          except OverflowError:
              raise ValueError(
                  f"Result overflow: {base}^{exponent} exceeds maximum float value"
              )