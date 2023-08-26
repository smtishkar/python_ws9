# Напишите декоратор, который сохраняет в json файл параметры
# декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию,
# которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json

def our_cash(func: callable):
    try:
        with open(f'{func.__name__}.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

        def wrapper(*args, **kwargs):
            arg = str(args) + str(kwargs)
            data_res = data.get(arg)
            if data_res:
                return data_res
            result = func(*args, **kwargs)
            data.update({arg: result})
            with open(f'{func.__name__}.json', 'w') as f:
                json.dump(data, f, indent=4)
            return result

        return wrapper


@our_cash
def sum(one, two):
    return one + two


@our_cash
def mult(one, two):
    return one * two

sum(3,5)
sum(3,6)
mult(2,8)