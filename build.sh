#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create superuser
DJANGO_SUPERUSER_USERNAME=dipshen \
DJANGO_SUPERUSER_EMAIL=di.pshennikova@yandex.ru \
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD} \
python manage.py createsuperuser --noinput || true 