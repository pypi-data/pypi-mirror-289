# 实现redis常用方法

import redis


class Redis:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)
    
    def set(self, key, value):
        return self.redis_client.set(key, value)
    
    def get(self, key):
        return self.redis_client.get(key)
    
    def delete(self, key):
        return self.redis_client.delete(key)
    
    def exists(self, key):
        return self.redis_client.exists(key)
    
    def keys(self, pattern='*'):
        return self.redis_client.keys(pattern)
    
    def mset(self, mapping):
        """ 批量设置键值对 """
        return self.redis_client.mset(mapping)
    
    def mget(self, keys):
        """ 获取多个键的值 """
        return self.redis_client.mget(keys)
    
    def setex(self, key, time, value):
        """ 设置过期时间 """
        return self.redis_client.setex(key, time, value)
    
    def ttl(self, key):
        """ 获取过期时间 """
        return self.redis_client.ttl(key)
    
    def incr(self, key):
        """ 增加数字值 """
        return self.redis_client.incr(key)
    
    def decr(self, key):
        """ 减少数字值 """
        return self.redis_client.decr(key)
    
    def lpush(self, name, value):
        """ 在列表左侧添加元素 """
        return self.redis_client.lpush(name, value)
    
    def rpush(self, name, value):
        """ 在列表右侧添加元素 """
        return self.redis_client.rpush(name, value)
    
    def lpop(self, name):
        """ 从列表左侧弹出元素 """
        return self.redis_client.lpop(name)
    
    def rpop(self, name):
        """ 从列表右侧弹出元素 """
        return self.redis_client.rpop(name)
    
    def llen(self, name):
        """ 获取列表的长度 """
        return self.redis_client.llen(name)
    