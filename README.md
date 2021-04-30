# TODO: PREPARE A GOOD README

# Redis
redis-server --port 6380 --slaveof 127.0.0.1 6379

# In the project folder
celery worker -A flask_ui.celery_client -E --pool=solo -l info

flower -A flask_ui.celery_client

python flask_ui.py

# In the project folder for REST-API
celery worker -A flask_api.celery_client -E --pool=solo -l info

flower -A flask_api.celery_client

python flask_api.py