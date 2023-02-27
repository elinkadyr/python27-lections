"=============Пакеты и модули============="
#module - любой файл с расширением .py
# import test
# print(test.a)

# from test import a
# print(a)

# package - набор модулей (в папке обязательно должен быть __init__.py)


# from package.test1 import hello
# hello()
# from package.test2 import list1
# print(list1)

"============Работа с файлами============"
# open - функция , позволяет открывать файлы в определенном режиме
# r - read (только для чтения)
# w - write (только для перезаписи, каждый раз при открытии очищает файл)
# a - append (только для дозаписи, добавляется в конец)
# x - создает файл, но если файл уже есть, - ошибка
# b - бинарный вид 

"read"
file = open('test.txt')
# если такого файла нет - выйдет ошибка
# если не указать режим - откроется в режиме чтения

'read', 'readable', 'readline', 'readlines'
print("readable", file.readable())  #True
print("writable", file.writable())  #False

print(file.read())       # считывает от начала до конца
print(file.read())       # '' потому что каретка в конце файла

file.seek(0)          #перенос каретки в начало (на индекс 0)
print(file.read()) 

file.seek(5)          #считываем от 5 индекса до конца
print(file.read()) 

file.seek(0)
print(file.read(5))          # считываем 5 символов 
print(file.read())          # считываем от 5 до конца

file.seek(0)   
print(file.readline())  #считывает до переноса enter (\n)
print(file.readline())  #считывает до переноса enter (\n)

file.seek(0)   
print(file.readlines())     # возвращает список  ['kadyrova\n', 'elina\n', 'emilbekovna\n']

file.seek(0)   
print(file.readlines(2))    #['kadyrova\n']

file.seek(10)   
print(file.tell())          #10

file.read()   
print(file.tell())          #27

# file.write('qwerty')   #io.UnsupportedOperation: not writable  #запись в режиме чтения запрещена

print(file.closed) #False
file.close() # !важно закрывать файлы!
print(file.closed) #True


# print(dir(file))


"Write"

file = open("new_file.txt", 'w')
#если файла нет - создает, если есть - очищает

# file.read()     #io.UnsupportedOperation: not readable   #чтение запрещено

file.write('kadyrova\n')
file.write('elina\n')

print(file.writelines(['el\n', 'kadyr'])) 

file.seek(0)
file.write('abc')

print("readable", file.readable())   #False
print("writable", file.writable())   #True

file.close()

"append"
file = open('new_file2.txt', 'a')
#если файла нет - создается новый

print("readable", file.readable())   #False
print("writable", file.writable())     #True

file.write('Hello') 
#дозапись идет в конец, старые данные не удаляются

file.seek(0)
file.write('New')


file.close()


'Контекстный менеджер'
# try:
#     file = open('abc.txt', 'w')
#     file.read
# except:
#     file.close()

with open ('test.txt') as f:
    f.read()
    print(f.closed) #False
# файл закрывается
print(f.closed)     # True