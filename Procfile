release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input
release: python3 manage.py createsuperuser

web: gunicorn core.wsgi
