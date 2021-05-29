web: gunicorn transpvisback.wsgi --log-file -
release: python manage.py makemigrations transparency && python manage.py makemigrations authentication && python manage.py migrate