"=======Числа======="

# int - целые числа

a = '5' 
print(type(a))

b = '5'
print(type(b)) # <class 'str'>

c = int('10')
print(type('c')) # <class 'int'>

# int ('5a')
# VAlueError: Invalid Literal for int () with base  10: 

# float - числа с плавающей точкой (дробные)

a = 10.5
print(type('a'))

b = float('15.3')
print(type(b))  # class 'float'

c = float(11)
print (c) # 11.0
print (0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1)

# decimal - точное дробное число
# Чтобы его использовать, нужно его импортировать

from decimal import Decimal
a = Decimal(0.1) # Мы уже передали не точное число

b = Decimal('0.1')
print(b + b + b + b + b + b + b + b + b + b)

# bin - бинарное число 
a = bin(10)
print(a) # 0b11
b = int(a, 2)
print(b) # 10

# hex - 16 система счисления
a = hex(15)
print(a) #0xf
b = int(a, 16)
print(b) #15

# complex - комплексные числа (3i+5j-7k+10)
a = complex(10, 3)
print(a)

"======Операции над числами======"
# 5 + 7 
# 8 - 3
# 2 * 3
# 10 / 5 # 2.0
# 10 // 5 # 2
# 5 % 2  остаток от деления 1
# 2 ** 3 возведение в степень (8=2*2*2)
# 25 ** 0.5 нахождение квадратного корня от числа (5)

# модуль числа - из отрицательного в положительное
abs(-5) # 5
abs(10) # 10

# pow 
# 1. возводит в степень 
# 2. находит остаток от деления на 3 число
pow(2,3)  # 8 = 2*2*2, 2**3
pow(2,3,4) # 0 = (2*2*2) % 4 

# divmod - 
# 1 число - целочисленное деление
# 2 число - остаток от деления
res = divmod(5,2)
print(res)
# 2 - 5 // 2   # 1 - 5 % 2
divmod(17,3)
# 5 - 17 // 3         # 2 - 17 % 3

# sqrt - нахождение квадратного корня 
from math import sqrt
sqrt(25)   #5
print(sqrt(25)) 
sqrt(9)  #3



