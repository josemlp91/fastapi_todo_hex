.PHONY: help

.DEFAULT_GOAL := help
runner=$(shell whoami)


help: ## This help.
	@echo
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo


build: ## Build developer containers.
	docker-compose build

up: ## Run developer containers.
	docker-compose up

makemigrations:
	docker-compose run --rm api alembic revision --autogenerate
	sudo chown -R $(runner):$(runner) -Rf *

migrate:
	docker-compose run --rm api alembic upgrade head

shell:
	docker-compose run --rm api ipython

bash:
	docker-compose run --rm api bash

silenceup: ## Run developer containers without print messages.
	docker-compose up -d

