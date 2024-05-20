build:
	docker compose build

run:
	docker compose up

stop:
	docker compose stop

logs::
	docker compose logs -f

tests::
	docker compose run tablebuilderbackend pytest

migrate:
	docker compose run tablebuilderbackend python manage.py migrate

makemigrations:
	docker compose run tablebuilderbackend python manage.py makemigrations

collectstatic:
	docker compose run tablebuilderbackend python manage.py collectstatic --noinput

clean:
	docker compose down -v

setup:
	@make build
	@make run
	@make logs

first_setup:
	cp example.env .env
	@make build
	@make run
	@make logs

full_build:
	@make build
	@make migrate
	@make collectstatic

restart:
	@make stop
	@make run
	@make logs