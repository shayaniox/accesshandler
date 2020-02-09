from datetime import timedelta

import redis
from nanohttp import settings


_redisconnection = None


def redisconnection():
    global _redisconnection
    if _redisconnection is None:
        _redisconnection = redis.Redis(**settings.redis_)

    return _redisconnection


def setkey(connection, ip, pattern, ttl):
    '''
    Sets a key including `ip` and `pattern` and a viewcount representing
    how many times an user from specific ip viewed a url which matches the
    pattern. Example:
        {"1.1.1.1::/foo/bar": "20"}

    If the `viewcount` is None, so it means it's the first view from ip.
    '''
    connection.setex(keystr(ip, pattern), ttl, 1)


def keystr(ip, pattern):
    return f'{ip}::{pattern}'


#async def start(name):
#    print('Message router started')
#    while True:
#        queue, message = await queues.bpop_async(name)
#        print(f'Processing message: {message}')
#        await route(ujson.loads(message))
#

