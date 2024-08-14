#!/usr/bin/env python3
"""
Using Redis NoSQL data storage
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    Represents an object for storing data
    """

    def __init__(self):
        """
        initilizing the Redis client and then flushing the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
