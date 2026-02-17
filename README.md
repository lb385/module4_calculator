# Module 4 Calculator

Simple modular calculator implementing operations, a calculation factory, history manager, REPL, and tests with CI.

Project structure

module4_calculator/
# Module 4 Calculator

A professional, modular command-line calculator with a REPL interface, factory
pattern, calculation history, and complete test coverage enforced via CI.

![CI](https://github.com/lb385/module4_calculator/workflows/Python%20application/badge.svg)

Features
- REPL interface with commands: `help`, `history`, `exit`
- Arithmetic operations: `add`, `sub`, `mul`, `div`
- `CalculationFactory` for creating calculations
- `History` manager to store session calculations
- Tests with `pytest` and CI that enforce 100% coverage

Project structure
```
module4_calculator/
├── app/
│   ├── calculator/
│   │   └── __init__.py
│   ├── calculation/
│   │   └── __init__.py
│   ├── operation/
│   │   └── __init__.py
│   └── main.py
├── tests/
├── .github/workflows/python-app.yml
├── requirements.txt
└── README.md
```

Setup
```bash
python3 -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate     # Windows (PowerShell/CMD)
pip install -r requirements.txt
```

Run the REPL
```bash
python -m app.main
```

Run tests
```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=100
```

Notes
- The repository ignores the `venv/` directory via `.gitignore` so the virtual
	environment is not committed.
- The GitHub Actions workflow at `.github/workflows/python-app.yml` runs the
	test suite and enforces 100% coverage on each push.
