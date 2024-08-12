
# 常用的装饰器函数
import time
import functools
import inspect

# 1. 日志记录装饰器
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} called at {start_time}, finished at {end_time}, duration: {end_time - start_time} seconds")
        return result
    return wrapper

# 2. 缓存装饰器
def cache_decorator(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

# 3. 权限检查装饰器
def permission_decorator(required_permission, get_user_permissions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_permissions = get_user_permissions()  # 假设这是一个获取用户权限的函数
            if required_permission not in user_permissions:
                raise PermissionError(f"User does not have permission {required_permission}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 4. 输入验证装饰器
def validation_decorator(schema):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = inspect.signature(func).bind(*args, **kwargs)
            for name, validator in schema.items():
                value = bound_values.arguments[name]
                if not validator(value):
                    raise ValueError(f"Validation failed for argument {name} with value {value}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 5. 性能测试装饰器
def performance_decorator(threshold=1e-3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            if duration > threshold:
                print(f"Function {func.__name__} took {duration} seconds, which is longer than the threshold {threshold}")
            return result
        return wrapper
    return decorator

# 6. 异常处理装饰器
def exception_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function {func.__name__} raised an exception: {e}")
            # 可以进行其他处理，比如记录日志、通知等
    return wrapper