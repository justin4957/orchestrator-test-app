"""Simple calculator module for testing orchestrator."""

import math
from typing import Union


class Calculator:
    """A basic calculator with common operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Raise base to the power of exponent.

        Args:
            base: The base number to be raised to a power.
            exponent: The exponent to raise the base to.

        Returns:
            The result of base^exponent as a float.

        Raises:
            TypeError: If base or exponent are not numeric types (int or float).
            ValueError: If the operation is mathematically undefined or results in
                overflow. Specifically:
                - When base is 0 and exponent is 0 (0^0 is undefined)
                - When base is negative and exponent is fractional (would result
                  in complex number)
                - When the result exceeds maximum float value (overflow)

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