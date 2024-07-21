install:
	poetry install

debug-mode:
	poetry run flask --app weather_website:app --debug run --port 8000

dev:
	poetry run flask --app weather_website:app run

PORT ?= 8000
#start:
#	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

#build:
#	./build.sh

lint:
	poetry run flake8 weather_website

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=weather_website --cov-report xml

selfcheck:
	poetry check

check: lint

.PHONY: install test lint selfcheck check build
