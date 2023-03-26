.PHONY: django-migrate django-start django-init start-app 

django-migrate:
	python manage.py migrate

django-dev:
	python manage.py runserver

django-start:
	gunicorn config.wsgi -b 0.0.0.0:8000

django-init: django-migrate
	python manage.py collectstatic --no-input

start-app: django-init django-start

build:
	docker build . -t url_shortener:sample

run:
	docker run -d --rm -it -p 8000:8000/tcp url_shortener:sample
