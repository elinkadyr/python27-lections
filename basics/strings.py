"========Строки========"
# строки - неизменяемый тип данных, предназнаенный для хранения текста или же последовательности символов
srting1 = 'строка в одинарных кавычках'
string2 = "строка в двойных кавычках"
string3 = "Don't"
string4 = 'Study in "Makers Incubator"'
string5 = '''Многострочный
текст - можно писать на 
нескольких строках
можно использовать любые кавычки'''
string6 = """Тут можно использовать 'Ciao bella'
любые кавычки"""

string7 = 'Hello' + ' ' + 'world' 
print (string7)

string8 = 'hello ' * 3
print (string8)

string9 = 'hello' + str(1)
print (string9)


"============Экранизация строк============"
'\n' # перенос на новую строку
print('hello\nworld') 

'\t' # отступ табуляция #TAB
print('hello    world') 

'\\' # экранизирует слеш \
print('hello \\ world ')

'\'' # отображение ' и "
print('hello \' world ')

'\r' # перенос каретки в начало строки
print('hello\rw')
print('123456789\rhello')

'\v' # перенос на новую строку со смещением вправо на длину пред. строки
print('shopokov\vbishkek')

"============Индексация============"
# индекс - порядковый номер символа в строке (начиная с 0)
'h e l l o'
#0 1 2 3 4

string10 = 'hello world'
print(string10[6])
index = len(string10) -1
print(string10[index])

string11 = 'hello world'
print(string11[-4])
#string [0] #первый символ
#string [-1] #первый символ с конца

#срез - часть строки
print(string11[6:9])
print(string11[0:6])
print(string11[:4])
print(string11[:-4])
print(string11[:])
print(string11[7:])
print(string11[0:11:2])
print(string11[::2])
print(string11[::-2])
print(string11[-3:-5:-1])

"=======Форматирование строк======="
title = 'Пирог'
price = 35
string = f'Название: {title}, Цена: {price}'
print(string)

format1 = 'Название: %s, Цена: %s'
print(format1 %('Яблоко', 80))

format2 = 'Название: {}, цена: {}'
print(format2.format('Груша', 60))

"===========Методы строк========"
# метод - функция, которая принадлежит определенному типу данных, обращаемся к ней через точку
# dir все доступные методы для данного типа данных 
#print (dir(str))
print('hello'.upper())
print('HELLO'.lower())
print('hello WORLD'.swapcase())
print('hello world'.title())
print('hello world'.capitalize())
print('hello world'.center(20))
print('hello world'.center(20, '-'))
print('hello world'.count('l'))
print('hello world'.count('ll'))
print('hello world'.count('Hello'))
print('hello world'.count(''))           #пустые строки между символами
print('hello world'.split())             # ['hello', 'world']
print('hello world'.split('o'))          #
print(' '.join(['hello', 'world']))      #hello world
print('%'.join(['hello', 'world']))      #hello%world
print('hello world'.find('w'))           #6
print('hello world'.rfind ('o'))        #7 поиск буквы с конца

string = '123456789a'
print(string.isalpha())
string = '123456789a'
print(string.isalnum())
string = '123456789a'
print(string.isdigit())



string1 = "Elina"
string2 = "Kadyrov"
print(string1[0] + string2[0] + string1[len(string1)//2] + string2[len(string2)//2] +string1[-1] + string2[-1])

string1 = 'Hello'
string2 = 'World'
print((string1+' '+string2+'\n')*3)

string1 = 'Hello'
string2 = 'World'
print(string1+' '+string2)
