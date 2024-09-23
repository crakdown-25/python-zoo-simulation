all: pytest mypy flake8

pytest:
	python3 -m pytest tests/*.py

mypy:
	mypy main.py

flake8:
	flake8 --max-line-length=130 `find . -name "*.py"`