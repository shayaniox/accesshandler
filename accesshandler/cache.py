from datetime import timedelta

import redis
from nanohttp import settings


_redisconnection = None


def redisconnection():
    '''
    Returns an global redis connection object.
    '''

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

    ...

    Parameters
    ----------
    connection : redis.Redis
    The redis connection
    ip : str
    The first part of storing key
    pattern : str
    The second part of storing key
    ttl : datetime.timedelta
    The expiry time of key value
    '''

    connection.setex(keystr(ip, pattern), ttl, 1)


def keystr(ip, pattern):
    '''
    Creates an string from `ip` and `pattern` with a seperator between

    ...

    Parameters
    ----------
    ip : str
    The first part of storing key
    pattern : str
    The second part of storing key
    '''

    return f'{ip}::{pattern}'

