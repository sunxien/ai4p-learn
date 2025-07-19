from functools import wraps


# 装饰器不指定名称
def a_decorator(func):
    print(f"enter a_decorator func....")
    @wraps(func)
    def wrap_func(a: int, b: int) -> int:
        print(f"enter wrap_func....")
        return func(a, b)
    return wrap_func

# This function to be decorated
@a_decorator
def add(a :int, b : int) -> int:
    return a + b

a1 = 2
b1 = 3
r1 = add(a1, b1)
print(f"{add.__name__}({a1}, {b1}) = {r1}")


# 装饰器指定名称
def b_decorator(name: str):
    print(f"enter b_decorator({name})....")
    def b_decorator_fun(func):
            @wraps(func)
            def b_decorator_wrapper(a: int, b:int):
                print(f"enter b_decorator_wrapper....")
                return func(a, b)
            return b_decorator_wrapper
    return b_decorator_fun


@b_decorator(name="minus_decorator")
def minus(a: int, b: int) -> int:
    return a - b

a2 = 22
b2 = 3
r2 = minus(a2, b2)
print(f"{minus.__name__}({a2}, {b2}) = {r2}")