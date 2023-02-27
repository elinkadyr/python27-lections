"============functions============"
#функции - именованный блок кода, который принимает аргументы и возвращает результат


#lambda - ключевое слово для создания анонимной функции
# func = lambda num1, num2: num1 + num2
# res = func(5, 10)
# print(res) #15
# print(func) #<function <lambda> at 0x7f6d420c7d90>

# #def - ключевое слово
# def my_sum(num1, num2):
#     return num1 + num2
# print(my_sum)   #<function my_sum at 0x7fc70e7e6050>
# res1 = my_sum(13, 45)
# print(res1)         #58

# def calc(num1, num2, oper):
#     """
#     oper - строка, с операцией для вычислений
#     '+' - сложение
#     '-' - вычитание
#     """
#     if oper == '+':
#         return num1 + num2
#     if oper == '-':
#         return num1 - num2
#     if oper == '*':
#         return num1 * num2
#     if oper == '/':
#         return num1 / num2
# print(calc(10, 12, '+'))    #22
# print(calc(20, 5, '-'))     #15
# print(calc(13, 7, '*'))     #91
# print(calc(145, 5, '/'))    #29
# print(calc(145, 5, 5))      #None

# def my_len(obj):
#     "Возвращает длину объекта"
#     count = 0 
#     for i in obj:
#         count += 1
#     return count

# print(my_len([11,2,23,4,4]))                #5
# print(my_len(['asa','add','ert','444']))    #4
# print(my_len({1:'a',2:'b'}))                #2

# def super_len(obj):
#     try:        
#         #если мы можем итерировать объект
#         return my_len(obj) 
#     except:
#         #если не можем, то будем итерировать его в виде строки
#         return my_len(str(obj))
# print(super_len([1,2,3,4]))         #4
# print(super_len(123456789))         #9
# print(super_len(None))              #4 'None'

"==============DRY=============="
#принцип    -   don't repeat yourself(не повторяйся)
# представим что нет функции len
# str_ = 'Hello world'
# count = 0
# for i in str_:
#     count += 1
#     print(count)        #11
# # count длина списка str_

# def len_(obj):
#     count=0
#     for i in obj:
#         count += 1
#     return count

"Аргументы и параметры"
# параметры - локальные переменные, значения которым мы задаем при вызове функции
# аргументы - значения, которые мы задаем параметрам при вызове функции

# def func(var):
#     local_var = 5
#     print(locals()) #{'var': 6, 'local_var': 5}

# func(6)

# print(local_var)     #NameError: 
# print(var)           #NameError


"=========Виды аргументов и параметров========="
#1 обязательный - 
#2 необязательный - 
#2.1 с дефолтным значением (по умолчанию)
#2.2 args (arguments)                = tuple 
#2.3 kwargs (key word arguments)     = dict

# def func(a):
#     print(a)
# func()        #TypeError
# func('hello')   #hello

# def func(a, b='default'):
#     print(a, b)
# func('hello')       #hello default
# func('hello', 100)  #hello 100

# def func(a, b='default', *args):
#     print(a, b, args)
# func('hello')       #hello default ()
# func('hello', 100) #hello 100 ()
# func('hello', 100, 84, 23, 'world') #hello 100 (84, 23, 'world')

"Виды аргументов"
# позиционные (по порядку параметров)
# именованные (по имени параметров)
# def func2(a,b):
#     print(f'a={a}, b={b}')

# # func2(10,20)           #a=10, b=20
# # func2(a=30, b=40)      #a=30, b=40
# func2(b=30, a=40)           #a=40, b=30

# def func(a, b='default', *args, **kwargs):
#     print(a, b, args, kwargs)
# func('hello')       
            #hello default ()
# func('hello', 100) 
            #hello 100 ()
# func('hello', 100, 84, 23, 'world')
            #hello 100 (84, 23, 'world')
# func('hello', 100, 84, 23, key1='world', key2='universe')   
            #hello 100 (84, 23) {'key1': 'world', 'key2': 'universe'}

"==========звездочки=========="
# list1 = [1,2,3,4]
# list2 = [*list1]      # list2 = [1,2,3,4]

# dict1 = {'a':1}
# list3 = [*dict1]          # dict2 = {**dict1} 
# list3 = ['a']             # dict2 = {'a':1}

# args - tuple, куда попадут все позиционные аргументы которые не попали по позиции
# kwargs - dict, куда попадут все именованные аргументы которые не попали по имени


"1"
# def add(x, z):      
#     return x + z  
# add(5, 5)
"2"
# def get_string_length(obj):
#     count=0
#     for i in obj:
#         count += 1
#     return count

# print(get_string_length('hello')) 
"3"
# def get_type(a,b):
#    return(f'{type(a)}\n{type(b)}')
# print(get_type(4,'el'))

# def get_type(x,y):
#      print(f'{type(x)}\n{type(y)}') 
# get_type(5,'s')
"4"
# def divide(x, z):      
#     return x / z  
# divide(5, 5)

"6"
# num = 6 
# def check(num): 
#     if num % 2 == 0: 
#         return("It is even number") 
#     else: 
#         return("It is odd number")
# print(check(num)) 
"7"
# def is_palindrome(str):
#     if str.upper() == str.upper()[::-1]: 
#         return True 
#     else: 
#         return False 
        
# print(is_palindrome("tot"))            #True
# print(is_palindrome("elina"))           #False
"8"
# def max_num(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max_num(5,2))
"9"
# def multiply_list(list_):
#     n = 1 
#     for i in list_: 
#         n *= i 
#     return n 
# print(multiply_list([45,45,77]))

"10"
# def sum_digits(num):
#     return(sum([int(x) for x in str(num)]))
# print(sum_digits(405617)) 

"11"
# def func11(a,b,c):
#     if c != 0:
#         return (a+b)/c
#     else:
#         return a+b
# func11(7,5,0)

"12"
# def func12(list1, b):
#     a = [] 
#     for i in list1: 
#         if b == 'lower': 
#             a.append(i.lower()) 
#         elif b == 'upper': 
#             a.append(i.upper())
#         return (a) 
# print(func12(["hEllo wORld"], 'upper'))

"14"
# def add_(a, b): 
#     return a + b 
# def sub_(a, b): 
#     return a - b 
# def mult_(a, b): 
#     return a * b 
# def div_(a, b): 
#     return a / b 
# def calc(num1,num2, oper): 
#     if oper == "+" :
#         return add_(num1, num2) 
#     elif oper == "-": 
#         return sub_(num1, num2) 
#     elif oper == "*": 
#         return mult_(num1, num2) 
#     elif oper == "/": 
#         return div_(num1, num2) 

# print(calc(40, 20, "+"))
"15"
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# def func15(users): 
#     r=[] 
#     for i in users: 
#         if i['work'].startswith('IT'): 
#             r.append(f"{i['name']}, скидки в магазине компьютерной техники!\n") 
#             h=''.join(i for i in r) 
#             return h 
# print(func15(users))

"17"
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]



"19"
# students = [ 
#     {'student': 'Jack', 
#         'marks': 43},
#     {'student': 'Tom', 
#         'marks': 92}, 
#     {'student': 'Helen', 
#         'marks': 85}, 
#     {'student': 'Peter',
#         'marks': 58},
#     {'student': 'Jessica', 
#         'marks': 78} 
# ] 
# def func19(list_:list): 
#     list_.sort(key=lambda x:x['marks'],reverse=True) 
#     return list_ 
# print(func19(students))

#Ответ
# [
# {'student': 'Tom', 'marks': 92}, 
# {'student': 'Helen', 'marks': 85}, 
# {'student': 'Jessica', 'marks': 78},
# {'student': 'Peter', 'marks': 58}, 
# {'student': 'Jack', 'marks': 43}
# ]

"20"


