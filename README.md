# Orchestrator Test Application
  
  A simple Python calculator application designed to test the self-reflexive-orchestrator's autonomous development capabilities.
  
  ## Purpose
  
  This project serves as an end-to-end test bed for the self-reflexive-orchestrator system, validating:
  - Issue analysis and claiming
  - Autonomous implementation
  - Pull request creation
  - Code review integration with multi-agent-coder
  - CI/CD monitoring
  - Automated merging
  - Bug tracking and documentation
  
  ## Application
  
  A basic calculator with operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Power
  - Square root
  
  ## Setup
  
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
  
  ## Usage
  
  ```python
  from calculator import Calculator
  
  calc = Calculator()
  
  # Basic operations
  result = calc.add(5, 3)        # Returns 8
  result = calc.subtract(10, 4)  # Returns 6
  result = calc.multiply(3, 7)   # Returns 21
  result = calc.divide(15, 3)    # Returns 5.0
  
  # Power operation
  result = calc.power(2, 3)      # Returns 8.0 (2^3)
  result = calc.power(5, 0)      # Returns 1.0 (any number^0)
  result = calc.power(2, -2)     # Returns 0.25 (2^-2 = 1/4)
  result = calc.power(4, 0.5)    # Returns 2.0 (square root of 4)
  result = calc.power(-2, 3)     # Returns -8.0 (negative base with integer exponent)
  
  # Square root
  result = calc.sqrt(16)         # Returns 4.0
  ```
  
  ### Power Operation Details
  
  The power operation supports:
  - **Positive exponents**: `calc.power(2, 3)` → 8.0
  - **Zero exponent**: `calc.power(5, 0)` → 1.0 (any non-zero number to power 0 equals 1)
  - **Negative exponents**: `calc.power(2, -2)` → 0.25 (returns reciprocal)
  - **Fractional exponents**: `calc.power(4, 0.5)` → 2.0 (equivalent to roots)
  - **Negative base with integer exponent**: `calc.power(-2, 3)` → -8.0
  
  **Important Edge Cases:**
  - `0^0` raises `ValueError` (mathematically undefined)
  - Negative base with fractional exponent raises `ValueError` (would result in complex number)
  - Very large results may raise `ValueError` for overflow protection
  
  ## Testing
  
  ```bash
  pytest
  ```
  
  Run with coverage:
  ```bash
  pytest --cov=calculator --cov-report=html --cov-report=term-missing
  ```
  
  ## CI/CD
  
  GitHub Actions will run:
  - Python linting (flake8)
  - Type checking (mypy)
  - Unit tests (pytest)
  - Coverage reports
  
  ## License
  
  MIT License