from django.conf import settings
import redis

REDIS_HOST = getattr(settings,'AIOHTTP_RQ_REDIS_HOST', "localhost")
REDIS_PORT = getattr(settings,'AIOHTTP_RQ_REDIS_PORT', 6379)
REDIS_DB = getattr(settings,'AIOHTTP_RQ_REDIS_DB', 0)
REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
