from functools import wraps

# 了解 __init__, __call__ 区别：
class MyDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        @wraps(self.func)
        def decorator_wrapper(a: int, b: int):
            print(f"enter decorator_wrapper....")
            return self.func(a, b)
        return decorator_wrapper

@MyDecorator
def add(a : int, b : int) -> int:
    return a + b

a1=22
b1=3
decorate_add = add(a1, b1)
print(f"add({a1}, {b1}) = {decorate_add(a1, b1)}")