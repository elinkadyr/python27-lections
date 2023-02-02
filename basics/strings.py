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
