worker: celery -A tasks worker --concurrency=1 --loglevel=info
web: python app/manage.py run_gunicorn -b 0.0.0.0:$PORT -w 3
