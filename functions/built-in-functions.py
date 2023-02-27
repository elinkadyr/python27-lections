"==================Встроенные функции=================="
# enumerate - функция принимаетпоследовательность и возвращает генератор

# list1 = [1,4,78,3,7,9,4,2,7]
# for ind, elem in enumerate(list1):
#     if ind % 2:
#         list1[ind] = elem * 2
#     if ind % 3 == 0:
#         list1[ind] = elem * 3
# print(list1)

# dict1 = {1:'a', 2:'b', 3:'c'}

# print(dict(enumerate(string,1)))

# list1 = [1,2,3,4,5]
# list2 = 'abcdefg'
# list3 = [0.5,0.3,0.6]

# print(list(zip(list1,list2,list3)))
# [(1, 'a', 0.5), (2, 'b', 0.3), (3, 'c', 0.6)]
"================Функция высшего порядка================"
# это функция которая:
# принимает аргументыв другую функцию
# возвращает функцию
# создает внутри функцию
# вызывает внутри функцию

# map - принимает в аргументы функцию, и итерируемый объект, возвращает генератор, в котором все элементы - это результат принимаемой функции,  в которую передали элементы последовательности
# mapped = map(int, ['1','2','3'])
# print(mapped)           #<map object at 0x7f17fa7fbfa0>
# print(list(mapped))     #[1, 2, 3]
# print(tuple(mapped))    #(1, 2, 3)
# print(set(mapped))      #{1, 2, 3}

# map(int, ['1','2','3'])
# int('1') -> 1     #int('2') -> 2  #int('3') -> 3

#дан список с числами, создать новый список, где элементы - числа из списка +1, с помощью map
'1'
#list1 = [1,2,3,4]
#def res1(i):
#     i += 1 
#     return i 
#print(list(map(res1, list1)))
'2'
#list1 = [1,2,3,4]
#def res1(i):
#     return i+1
#print(list(map(res1, list1)))
'3'
# list1 = [1,2,3,4]
# print(list(map(lambda i: i+1, list1)))      #[2, 3, 4, 5]


# filter - принимает в аргументы функцию, и итерируемый объект, возвращает генератор, в котором элементы из последовательности прошедшие фильтр (функция вернула True)
'1'
#list1 = [-31,25,-345,23,0,4,12]
#def is_positive(i):
#    return i > 0 
#print(list(filter(is_positive, list1)))     #[25, 23, 4, 12]
'2'
#list1 = [-31,25,-345,23,0,4,12]
#print(list(filter(lambda i: i>0, list1)))       #[25, 23, 4, 12]


#дан список со строками, оставить только те строки которые начинаются с большой буквы
# list1 = ['Hello', 'world', 'MAKERS']
'1'
# # print(list(filter(lambda i: i[0].isupper(), list1))) 
'2'
# # res = [i for i in list1 if i[0].isupper()]
# # print(res)
'3'
# def first_is_upper(word):
#     first = word[0]
#     return first.isupper()
# print(list(filter(first_is_upper, list1)))    #  ['Hello', 'MAKERS']


# reduce - функция которая импортируется из модуля functools, 
# тоже принимает функцию и итерируемый объект, возвращает один результат

# from functools import reduce

# list1 = [2,4,6,8,10]
'example'
# def mul(x,y):
#     return x*y
# print(reduce(mul, list1))       #3840
'example'
# string = 'hello world'
# print(reduce(lambda i,y: i+'$'+y, string))  #h$e$l$l$o$ $w$o$r$l$d

#дан список со словами, вывести слово с большим количеством букв
# list1 = ['hello', 'world', 'makers', 'bootcamp']
'1'
# print(reduce(lambda i,y: i if len(i)>len(y) else y, list1)) 
'2'
# def func(x,y):
#     if len(x)==len(y):
#         return x
#     return y
# print(reduce(func, list1))

# n = 5
# while n > 0: !
#     n -= 1
#     print(n)

res = [1,2,4,3,5]
res.insert(2,88)
print(res)