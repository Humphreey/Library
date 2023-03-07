'''
Простейший декоратор
'''
def example1():
    x = 11

    def inner():
        print(f'Переменная из замыкания: {x}')

    return inner

# example1()()
# Переменная из замыкания: 11

print()
'''
Вызов декоратора
'''

def example2(func):

    def inner():
        print('Начало работы декоратора...')
        func()
        print('Декоратор отработал!')
    return inner

# Вариант 1
# @example2
# def print_hi():
#     print('Привет, я - функция, которую задекорировали!')

# Вариант 2
#print_hi = example2(print_hi)
# print_hi()
# Начало работы декоратора...
# Привет, я - функция, которую задекорировали!
# Декоратор отработал!

print()
'''
Декорирование функции с аргументами
'''
def decorate_func_with_params(func):

    def inner(*args, **kwargs):
        print(f'Декорируем функцию с параметрами: {args}, {kwargs}')
        func(*args, **kwargs)
        print('Все прошло успешно!')
    return inner


@decorate_func_with_params
def adder(*nums):
    print(sum(nums))

# adder(1,2,3)

print()
'''
Декоратор с параметрами
'''
def repeater(num_of_repeats=1):
    def outer_decorator(func):
        def inner_decorator(*args, **kwargs):
            if num_of_repeats > 0:
                for _ in range(num_of_repeats):
                    print(func(*args, **kwargs))
            else:
                print(func(*args, **kwargs))
        return inner_decorator
    return outer_decorator

@repeater(3)
def print_text(message):
    return f'Вам сообщение: {message}'

# print_text('Время программировать!')

print()
'''
Декоратор как класс
'''
class Numerator:
    def __init__(self, func):
        self.func = func
        self.counts = 0

    def __call__(self, *args, **kwargs):
        self.counts += 1
        print(self.counts)
        return self.func(*args, **kwargs)


@Numerator
def info_func(*args, **kwargs):
    return args, kwargs
# print(info_func(2, 3, p=100))
# print(info_func(2, 3, p=100))
