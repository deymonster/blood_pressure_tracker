.PHONY: build run stop migrate makemigrations createsuperuser

build:
	docker-compose build

run:
	docker-compose up -d

stop:
	docker-compose down

migrate:
	docker-compose run --rm web python manage.py migrate

makemigrations:
	docker-compose run --rm web python manage.py makemigrations

createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser