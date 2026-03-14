# Python 装饰器

# 简单装饰器
def my_decorator(func):
    def wrapper():
        print("调用前")
        func()
        print("调用后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 带参数的装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回 {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(1, 2)

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet():
    print("Hello!")

greet()

# 内置装饰器
class MyClass:
    @property
    def value(self):
        return self._value

    @staticmethod
    def static_method():
        print("静态方法")

    @classmethod
    def class_method(cls):
        print("类方法")
