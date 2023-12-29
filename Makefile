setup:
	python3.10 -m pip install poetry

install:
	poetry install

test:
	poetry run pytest -ssv --cov --cov-report=html

build:
	poetry build

publish: build
	poetry publish

format:
	poetry run black greps/ tests/

lint:
	poetry run ruff greps/ tests/
	poetry run mypy greps/ tests/