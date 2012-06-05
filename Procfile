web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT myblog/settings.py
worker: bin/python myblog/manage.py celeryd -E -B --loglevel=INFO