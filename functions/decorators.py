'========Декораторы========'
#функция высшего порядка, которая нужна чтобы расширять функционал другой функции не меняя её

# def decorator(func):
#     def wrapper():
#         print('Функция вызывается')
#         func()
#         print('Функция завершила работу')
#     return wrapper

# def func():
#     print('hello')

# res = decorator(func)
# print(res)             
#                         #<function decorator.<locals>.wrapper at 0x7f3f3b8e63b0>
# res()
#                         # Функция вызывается
#                         # hello
#                         # Функция завершила работу

'===========Синтаксический сахар==========='

# def decorator(func):
#     def wrapper():
#         print('Функция вызывается')
#         func()
#         print('Функция завершила работу')
#     return wrapper

# @decorator
# def func():
#     print('hello')

# func()

# print(func)         #принтится  декоратор фанк <function decorator.<locals>.wrapper at 0x7f45411aa440>

# @decorator
# def func(string):
#     print(string)

# func('hello')

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return wrapper

# def func(*args, **kwargs):
#     print(args, kwargs)  

# func(10, 40, 50, a=4, b=6)   

# def func(a,b):
#     print(a,b)

# func(4,5)
# dict_ = {'a':10, 'b':12}
# func(**dict_)
# tuple_ = (1,2)
# func(*tuple_)

# from datetime import datetime

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         end = datetime.now()
#         print(f'Функция отработала за {end-start}')
#     return wrapper

# @timer
# def func(count):
#     for i in range(count):
#         print(i)
# # func(1000)
# @timer
# def func(a,b):
#     print(a,b)

# func(1,4)


# from functools import cache

# @timer
# @cache
# def func(count):
#     return sum(range(count))

# func(1000)
# func(100)
# func(100)


list1 = (1,2,3)
print(list1[::])
print(dir(dict))

for i in range(5):
    if i==3:
        break
    print(i)

