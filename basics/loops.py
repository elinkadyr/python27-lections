"===============Циклы==============="
#цикл - блок кода, который отрабатывается несколько раз
#for - цикл, который работает с итерируемыми объектами, цикл закан.ет свою работу когда он доходит до последнего элемента в итерируемом объекте 
#while - цикл, который работает до тех пор, пока условие верное

# list1 = ['hello', 10, True, [1,2,3]]
# for element in list1:
#     print(element)

# string1= 'Hello world'
# for letter in string1:
#     print(letter)
# #CTRL + C ЧТОБЫ ОСТАНОВИТЬ

# i = 1
# while i != 10:
#     print('hello', i)
#     i = i + 1
 
# i = 0
# while i:
#     print('Hello world')
#     i = i + 1 #вообще не отработает потому что 0 = false

# "================Ключевые слова в циклах================"
# #break - полностью останавливает цикл
# #continue - переход к след. итерации

# for i in range(10):
#     if i == 3:
#         break
#     print(i)        


# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

# for i in range(10):
#     print(i)
#     break
# #0

# list2 = [1,2,3,4,3,4,3,1,1,]
# for x in list2:
#     if 1 in list2:
#          list2.remove(1)
# print(list2)

# list2 = [1,2,3,4,3,4,3,1,1]
# while 1 in list2:
#     list2.remove(1)
# print(list2)


# labels = ['Honda', 'Kawasaki', 'Mazda']
# for x in labels:
#     print('I like brand ' + x)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for res in nums:
#     if res > 5:
#         break
# print(nums)

# list_ = [4, 3, 2, 1, 10, 14, -14]
# for new_list in list_:
#     list_.append(str(new_list))
# print(new_list)

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# colors1.extend(colors2)
# print(colors1)

# name_of_list = ['Helloworld!'] 
# string = name_of_list[0]

# len_ = len(string)

# if len_ % 2 == 0:
#     one = string[:len_ // 2]
#     sec = string[len_ // 2:]
# else:
#     one = string[:(len_ // 2) + 1]
#     sec = string[(len_ // 2) + 1:]

# new_list = list(sec) + list(one)
# print(new_list)

# a = {
#     'x': 1,
#     'y': 2, 
#     'z': 1
# }
# print(a['x'])

# fruits = ['яблоко', 'банан', 'апельсин']
# for fruit in fruits:
#     print(fruit)

# dic = {
#     1 : 'a',
#     2: 'b'
# }

# a = [1, 2, 3]
# b = a.copy()
# # b.append(4)
# print(id(a))
# print(id(b))

# key=lambda x: x[-1]

# a = ['johnb', 'elin', 'fan']
# a.sort(key=lambda x: x[-1])
# print(a)

# string = 'hello erty'
# for char in string:
#     print(char)

# # my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # for inner_list in my_list:
# #     print(inner_list)

# users = ('John', 'Kate','Alex')

# for key in users:
#     print(key, end='*******')

# # 
# string = 'hello'
# for char in string:
#     print(char)

# edibles = ["отбивные", "пельмени", "яйца", "орехи"]

# for food in edibles:
#     if food == "пельмени":
#         print("Я не ем пельмени!")
#         continue
#     print("Отлично, вкусные " + food)
# else:
#     print("Ненавижу пельмени!")
# print("Ужин окончен.")

# for i in 'Python':
#     print(i, end='*')

# res = [1,2,3]
# res.pop()
# print(res)

'======================методы======================'
# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# print(dir(int))
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'

# print(dir(str))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

# print(dir(dict))
# #'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

# print(dir(tuple))
# 'count', 'index']

print(dir(frozenset))
'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union'
'======================методы======================'


# list1 = [1,2,3]
# list1.pop(4)
# print(list1)    #IndexError

# list1 = ['a', 'b']
# list1.remove('c')
# print(list1)        #ValueError


