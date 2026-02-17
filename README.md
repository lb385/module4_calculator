# Module 4 Calculator

Simple modular calculator implementing operations, a calculation factory, history manager, REPL, and tests with CI.

Project structure

module4_calculator/
├── app/
│   ├── calculator/
│   ├── calculation/
│   ├── operation/
│   └── main.py
├── tests/
└── .github/workflows/python-app.yml

How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=100
```
