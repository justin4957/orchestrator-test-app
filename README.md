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

## Testing the Orchestrator

Issues will be created with varying complexity levels to test the orchestrator's:
1. Simple feature additions
2. Bug fixes
3. Refactoring tasks
4. Test coverage improvements
5. Documentation updates

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
result = calc.add(5, 3)  # Returns 8
```

## Testing

```bash
pytest
```

## CI/CD

GitHub Actions will run:
- Python linting (flake8)
- Type checking (mypy)
- Unit tests (pytest)
- Coverage reports

## License

MIT License
