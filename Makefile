APP_NAME=devex-app

up:
	docker compose up --build

down:
	docker compose down

test:
	docker compose run --rm app pytest

lint:
	docker compose run --rm app flake8 app.py

clean:
	docker compose down -v --remove-orphans

docs:
	python scripts/ai_pr_summary.py
