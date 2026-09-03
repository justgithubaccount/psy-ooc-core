UV = uv

.PHONY: install run-server test simulate format lint check clean-pyc clean

install:
	$(UV) sync

run-server:
	$(UV) run uvicorn ooc.api.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(UV) run pytest

simulate:
	$(UV) run ooc simulate

format:
	$(UV) run black src tests
	$(UV) run ruff check --fix src tests

lint:
	$(UV) run ruff check src tests
	$(UV) run black --check src tests

check: lint test

clean-pyc:
	find . -name "*.py[co]" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

clean: clean-pyc
	rm -rf dist build *.egg-info .pytest_cache .mypy_cache .ruff_cache
