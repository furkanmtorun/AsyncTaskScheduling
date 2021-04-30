# Redis
redis-server --port 6380 --slaveof 127.0.0.1 6379

# In the project folder
celery worker -A server.client -E --pool=solo -l info
flower -A server.client
python server.py

# In the project folder for REST-API
celery worker -A api.celery_client -E --pool=solo -l info
flower -A api.celery_client
python api.py