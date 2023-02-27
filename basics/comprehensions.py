"============Comprehensions====="
# генератор с помощью которого можно создавать последовательность, используя цикл FOR

# list1 =[]
# for i in range(1, 11):
#     list1.append(i)
# print(list1)      #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list1 = [i for i in range(1, 11)]
# print(list1)  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list1 = [i**2 for i in range(1, 11)]
# print(list1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# результат for элемент in последовательность 
# результат for элемент in последовательность if фильтр

# сomprehension = (i for i in range(1,11))
# print(сomprehension)  # <generator object <genexpr> at 0x7f88134d66c0>

#генератор - итерируемый объект, который не хранит в себе полностью все элементы послед-ти, а генерируют 

# print(next(comprehension))   #1

#next - функция, которая принимает в себя генератор, запрашивает следующий элемент у генератора и возвращает его

# сomprehension = (i for i in range(1,11))
# print(list(сomprehension))      #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(сomprehension))       #[]
# сomprehension

"============Синтаксический сахар============"
#list comprehension
# list_compr = [i for i in 'hello']
# print(list_compr)       #['h', 'e', 'l', 'l', 'o']

#dict comprehension
# dict_compr = {i: str(i) for i in range(1,11)}
# print(dict_compr) #{1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

#фильтр
# string = 'HellO WorLD'
# res = [i for i in string if i.islower()]
# print(res)      #['e', 'l', 'l', 'o', 'r']

# создать список состоящий из чисел от 1 до 10 из четныйх 
# list1 = [i for i in range(1, 11) if i % 2 == 0]
# print(list1)              #[2, 4, 6, 8, 10]

# list2 = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list2.append(i)
# print(list2)       # [2, 4, 6, 8, 10]

# res = [i for i in range(2,22,2)]
# print(res)      #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# =========создать список из чисел от 1 до 10 
# res = [i*100 for i in range(1,11)]
# print(res)  #[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# =======создать список 'hello' 5 раз
# res = ['hello' for i in range(5)]
# print(res)  #['hello', 'hello', 'hello', 'hello', 'hello']

#======Создать список
# res = ['test1', 'test2', 'test3']
# # for i in res:
# #     print(f'Hello {i}')         #Hello test1 Hello test2 Hello test3

# name = ['test1', 'test2', 'test3']
# z = ['hello ' + name for name in range(1,3)]
# print(z)

#======создать список в котором 5 списков с диапазоном 
# res = [[x for x in range(1, i+1)] for i in range(1,6)]
# print(res)      #[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

# res = []
# for i in range(1,6):
#     inner_list = []
#     for x in range(1, i+1):
#         inner_list.append(x)
#     res.append(inner_list)
# print(res)          #[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

#==============
# list1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# res = [1,2,3,4,5,6,7,8,9,10,11,12]

# # res1 = [i for inner_list in list1 for i in inner_list]

# # res = []
# # for inner_list in list1:
# #     for i in inner_list:
# #         res.append(i)
# print(res)
#==================

# res = ['четное' if i%2==0 else 'не четное' for i in range(1,7)]
# print(res)

#============
# dict1 = {'a':1, 'b':2, 'c':3}
# ==1==
# res = {v:k for k, v in dict1.items()}
# print(res)      #    {1: 'a', 2: 'b', 3: 'c'}
# ==2==
# res = {}
# for k,v in dict1.items():
#     res.update({v:k})
# print(res)

#=========
# res = {i:[x for x in range(1, i+1)] for i in range(1,6)}
# print(res)

# # set comprehension
set_comp = {x for x in range(11)}
print(set_comp)


'если мы не будем использовать переменную можно просто испльзовать _ '