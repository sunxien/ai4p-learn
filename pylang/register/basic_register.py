registers = {}


def reg_func():
    pass

lam_func = lambda x : x + 1

def cls_func(cls):
    pass

registers[reg_func.__name__] = reg_func
registers[lam_func.__name__] = lam_func
registers[cls_func.__name__] = cls_func

print(registers)