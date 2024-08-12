import os
import json
import time


class LocalCache:
    def __init__(self, cache_file='./cache.json'):
        self.cache_file = cache_file
        if not os.path.exists(cache_file):
            with open(cache_file, 'w') as f:
                json.dump({}, f)

    def get(self, key):
        with open(self.cache_file, 'r') as f:
            data = json.load(f)
            if key in data and time.time() < data[key]['expiration_time']:
                return data[key]['value']
        return None

    def set(self, key, value, timeout=None):
        with open(self.cache_file, 'r') as f:
            data = json.load(f)
        expiration_time = time.time() + (timeout or 0)
        data[key] = {'value': value, 'expiration_time': expiration_time}
        with open(self.cache_file, 'w') as f:
            json.dump(data, f)

    def delete(self, key):
        with open(self.cache_file, 'r') as f:
            data = json.load(f)
        if key in data:
            del data[key]
        with open(self.cache_file, 'w') as f:
            json.dump(data, f)

    def clear(self):
        with open(self.cache_file, 'w') as f:
            json.dump({}, f)


def cache_decorator(func):
    def wrapper(*args, **kwargs):
        key = json.dumps((args, kwargs))
        local_cache = LocalCache()
        cached_value = local_cache.get(key)
        if cached_value:
            return cached_value
        result = func(*args, **kwargs)
        local_cache.set(key, result)
        return result

    return wrapper


cache = LocalCache()

# Example usage:
if __name__ == "__main__":
    cache.set('foo', 'bar')
    print(cache.get('foo'))  # Output: bar
    time.sleep(1)
    print(cache.get('foo'))  # Output: None (after timeout)
