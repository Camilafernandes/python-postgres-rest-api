from flask_caching import Cache

cache = Cache(config={ 
        'CACHE_REDIS_HOST': 'redis',
        'CACHE_REDIS_PORT': '6379'})
