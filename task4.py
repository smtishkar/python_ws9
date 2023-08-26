def param(count: int):
    def deco(func):
        my_list = []
        def wrapper(*args, **kargs):
            for i in range(count):
                result = func(*args, **kargs)
                my_list.append(result)
            return my_list
        return wrapper
    return deco


@param(3)
def sum_(a, b):
    return a + b

print(sum_(2, 4))