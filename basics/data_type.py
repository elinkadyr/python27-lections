'______________________Переменные__________________'
# переменные - это именнованные ссылки на ячейки памяти, где хранятся какие то данные, для дальнейшего использовнаия, при обращении к названию переменной
num1 = 15
num2 = 10
print(num1 + num2)

"_________________Ввод и вывод данных_________________"
# input - фунция, которая позволяет принимать данные с терминала
# print - функция, которая позволяет выводить данные в терминал

number = input("Введите число: ")
print("Введенное число -", number)

____________ "Правила наименования переменных" ____________
a = 5 #можно, но не совсем понятно
1num = 10 #нельзя начинать с чисел
hello_world = 'hello world' #для разделителя можно использовать только _ (нижнее подчеркивание)
print = 'print'  #не стоит называть переменные уже встроенными названиями
if = 4  #не получится использовать в качестве переменных ключевые слова

# Snake Case - python стиль написания перемемнных

# Camel Case -стиль написания переменных во всех других языках программирования

__________________"Типы данных в Python"__________________
# неизменяемые типы данных
int_ = 17 
float_ = 34,0
str_ = 'hello'
bool_1 = True
bool_2 = False
none_ = None
tuple_ = (1,2,3,4,5,6,7,8,9,10)

# изменяемые типы данных
list_ = [1,2,3,4,5,6,7,8,9,10]
set_ = {1,2,1,4} # {1,2,4}
dict_ = {'a':1, 'b':2, 'c':3}

