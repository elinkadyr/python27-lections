"================Кортеж================"
# tuple - неизменеямый, итерируемый, индексируемый, упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке (в целом ничем не отличается от списков, просто неизменяемый, поэтому занимает меньше памяти)

# tuple1 = (1,2,3,4)  #type-tuple
# tuple1 = (5)        #type-int
# tuple3 = 1,2,3,4    #type-tuple 
# tuple4 = 5,         #type-tuple(5,)
# tuple5 = (1, 'hello', [1,2,3])
# tuple5[-1].append(4)       #(1, 'hello', [1, 2, 3, 4])
# tuple5[0] = 5   #TypeError: 'tuple' object does not support item assignment
# tuple6 = tuple('hello') #('h', 'e', 'l', 'l', 'o')

"==============Методы tuple=============="
# print(dir(tuple))
#count - считает количество данного элемента в tuple
tuple1 = (1,2,3,4,5)
print(tuple1.count(1))
print(tuple1.count('hello'))

#index - возвращает индекс данного элемента в tuple
tuple2 = ('hello', 'world', 105)
print(tuple2.index('hello'))    #0
print(tuple2.index('w'))        #ValueError: tuple.index(x): x not in tuple

