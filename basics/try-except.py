"=======exceptions======="
# Исключения (ошибки) - объеты, которые обрывают работу кода если не были обработаны

SyntaxError          #Ошибка, которое выходит если допущена синтаксическая ошибка
                # (         
                # ''' SyntaxError: '(' was never closed '''
TabError              #Ошибка
IndentationError      #когда не соблюдаем отступы
TypeError   #исключение, которое выходит когда мы делаем что-то не свойственное данному типу данных
                # 1 + '1'  -     
                # ''' TypeError: unsupported operand type(s) for +: 'int' and 'str''''
                # когда мы передаем функцию больше или меньше аргументов, чем она требует

KeyError        #когда мы обращаемся по несуществующему ключу, в словаре

NameError       #если нет такой переменной

ValueError      #когда мы передаем в функцию то , что она не может корректно обработать, когда мы пытаемся 
                #распаковать нетакое количество элементов в несколько переменных

AttributeError  #когда пытаемся обратиться к несуществующему методу в каком-то типе данных
                #"""AttributeError: 'dict' object has no attribute 'max'"""

IndexError      #когда обращаемся по несуществующему индексу

ModuleNotFoundError     #когда пытаемся обратиться к несуществующей библиотеке

ZeroDivisionError       #когда делим на ноль




Exception           #исключение, которое создали чтобы его вызвать
                    #чтобы вызвать исключение используем raise('hello')


"==================обработка исключений=================="
#чтобы код не ломался , можно использовать конструкцию try-except и обработать исключение
# try:
#     # код, который возможно вызовет ошибку
#     num = int(input('Введите число: '))
# except ValueError:
#     # код который отработает только если в блоке try вызвалась ошибка ValueError
#     print("вы ввели не число")
# else:
#     # код, который отработает толкьо если в блоке try ни одна ошибка не вызвалась
#     print("Введенное число:", num)
# finally: 
#     #код который отрабатывает вообще в любом в случае
#     #хоть вызвалась ошибка или нет
#     print("До свидания")
#минимальная конструкция состоит из try-except или try-finally
#можно использовать несколько except

# try:
#     num1 = int(input("Введите 1 число "))
#     num2 = int(input("Введите 2 число "))
#     print(num1 // num2)
# except(ValueError, ZeroDivisionError):
#     print('Введены не корректные данные')
# можно отловить любые исключения просто используя except


# try:
#     raise NameError
# except:
#     print('Любая ошибка')

# try:
#     print(1+'1')
# except TypeError:
#     try:
#         print(int('10a'))
#         print('a')
#     except ValueError:
#         print('аа')
# except ValueError:
#     print('b')
# finally:
#     print('c')

# можно отловить любые ошибки отлавливая Exception
# try:
#     raise ValueError
# except Exception as e:
#     print(type(e))
"1"
# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass
"2"
# try: 
#     b = 10
#     c = 11 
#     print(a)
# except NameError: 
#     print('Такой переменной не существует!')
"3"
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1/num2)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
"4"
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 + num2)
# except (TypeError, ValueError):
#     print('Введите число!')
"5"
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key1'])
# except KeyError:
#     print('Нет такого ключа!')
# "6"
# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[0])
# except IndexError:
#     print('Нет такого элемента!')

"7"
# try: 
#     age = int(input()) 
#     if age < 18: 
#         raise ValueError('Доступ запрещён') 
# except ValueError: 
#     print('Введён некорректный возраст') 
# else: 
#     print('Спасибо') 
# finally: 
#     print('До свидания!')

# "8"
# try:
#     num1 = float(input())
#     num2 = float(input())
#     print(num1/num2)
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')
"9"
# try: 
#     cash = int(input()) 
#     if cash < 0:
#         raise Exception ('ValueError')
#     print(cash) 
# except: 
#     print('Сумма не может быть отрицательной!')
"10"
# list_ = [1, 2, 3] 
# try: 
#     print(list_.get(0)) 
# except AttributeError: 
#     print(list_[0])
"11"
# string = 'hi'
# num = 5
# try:
#     print(string+num)
# except TypeError:
#     print('Unsupported option')
"12"
# try:
#     for x in range(10):
#         list_.append(x) 
# except: 
#     print([0,1,2,3,4,5,6,7,8,9])
"13"
# list_ = [1, 2, 3, 4]
# try:
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     for i in range(0, len(list_)): 
#         print(list_[i])
"14"
# password = "elina66"
# try:
#     if len(password)<6: raise ValueError
# except:
#         raise ValueError
"15"
# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]
# for i in warehouse: 
#     if len(warehouse)>10 or len(i)>3: 
#         raise ValueError()

"21"
# try: 
#     inp1 = input() 
#     inp2 = input() 
#     print(int(inp1) + int(inp2)) 
# except: 
#     print(inp1+inp2)

#"22"


# def func():
#     try:
#         return 0
#     finally:
#         return 1
# print(func())

# def is_palindrom(obj):
#     try:
#         return obj == obj[::-1]
#     except TypeError:
#         return str(obj)==str(obj)[::-1]
    
# is_palindrom('топот')

# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# if num > 0:
#     res = 'positive'
# else:
#     if num < 0:
#         res = 'negative'
#     else:
#         res = 0
# print(num)