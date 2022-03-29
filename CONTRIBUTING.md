# Contributing

Set up dev environment:
```shell
cd ~/your/repository/fork  # Activate venv if you have one (recommended)
poetry install             # Install all dependencies 
pre-commit install         # Install git pre-commit hooks
```

Run unit tests with coverage:

```shell
py.test --cov=python_aioarango --cov-report=html  # Open htmlcov/index.html in your browser
```

Build and test documentation:

```shell
python -m sphinx docs docs/_build  # Open docs/_build/index.html in your browser
```

Thank you for your contribution!
