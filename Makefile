# Including commands
run-django-server:
	poetry run task server localhost:8000

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

.PHONY: migrations
migrations:
	poetry run task makemigrations

.PHONY: test
test:
	poetry run task test

# Primary commands
.PHONY: install
install:
	poetry run pip install -U setuptools
	poetry install --no-root
	poetry run task initconfig --debug
	@make migrate
	poetry run task defaultadmin

.PHONY: run
run:
	@make run-django-server
