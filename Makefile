# Значение по умолчанию
MODE ?= dev

COMPOSE_FILE := docker-compose.$(MODE).yml

.PHONY: build up down logs

build:
	docker compose -f $(COMPOSE_FILE) build

up:
	docker compose -f $(COMPOSE_FILE) up

down:
	docker compose -f $(COMPOSE_FILE) down

logs:
	docker compose -f $(COMPOSE_FILE) logs -f