web: venv/bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT myblog/settings.py
worker: venv/bin/python myblog/manage.py celeryd -E -B --loglevel=INFO
celeryd: python manage.py celeryd -E -B --loglevel=INFO