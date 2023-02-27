"=============Списки=List============="
# списки - изменяемый, итерируемый, индексируемый, упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке

# list1 = [1, 3.4, 'hello', [1,2,3], (1,2), None, True, False]
# list1[0] #10
# list1[3] #1,2,3
# list1[3][-1] #3  

# list2 = list('hello')
# print(list2)

#конструктор list перебирает по объектам
#например list'hello'  -> ['h', 'e', 'l', 'l', 'o']
#[] #() #{}

        #функция (начинается с 3, до 10, с шагом 2)
#list3 = list(range(3,10,2))
#print(list3)  # -> 3, 5, 7, 9

"==============Изменяемость=============="
# string = 'hello'
# res = string.upper()
# print(string)   #'hello'
# print(res)      #'HELLO'

# list1 = []
# list1.append(1)
# list1.append(2)
# list1.append(3)
# print(list1)

# a = 10
# b = 10
# print(id(a))
# print(id(b))

"============Методы списков============"
# append - метод, который добавляет элемент в конец списка
# list1 = []       #литералы списков - #[]
# list1.append('hello')
# list1.append(500)
# list1.append([1,2,3])
# print(list1)

# remove - метод который удаляет элемент из списка по значению, но только первое вхождение, выдаст ошибку ValueError если такого элемента нет в списке
# list2 = ['hello', 500, 'world', 1000, 'hello', 500]
# list2.remove('hello')
# print(list2) [500, 'world', 1000, 'hello', 500]

# pop - метод который удаляет элемент из списка по индексу, если этого индекса нет, выдаст IndexError
# list3 = [10, 20, 30, 40, 50]
# list3.pop()
# print(list3) #[10, 20, 30, 40]
# list3.pop(1)
# print(list3) #[10, 30, 40]

# list = []
# list.pop()
# IndexError: pop from empty list

#также метод pop возвращает удаленный элемент
# list4 = [10, 20, 30, 40]
# popi = list4.pop(0) 
# print(list4)        #[20, 30, 40]
# print(popi)         #10

#insert - метод, который добавляет элемент в список по индексу 
# list5 = [1, 2, 3, 4]
# list5.insert(0, 'hello')
# print(list5)

# list14 = list(range(1,21))
# print(list14)

# list = [1,2,3,4,5,6,7,8,9,10]
# res = list[::-1]
# print(res)

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1.reverse()
# print(list1)

#count -  считает количество элемента который передаем в метод в списке
# list2 = [1, 2, 1, 4, 5, 1, 7, 8, 9, 1]
# print(list2.count(1))

# #index - возвращает индекс данного элемента
# list4 = ['hello', 'world', 'makers']
# print(list4.index('makers'))
# ind1 = list4.index('hello')
# print(ind1)

# # sort  
# list5 = [21,34,11]
# print(list5.sort())

# # copy - возвращает копию списка
# list1 = [1,2,3]
# list2 = list1.copy()
# list2.append(4)
# print(list1)
# print(list2)

# # extend - расширяет список другим списком
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list1.extend(list2) 
# print(list1)
# print(list2)

# string = 'elinkaaaaaa'
# print(string[:5]+'K'+string[6:])

# a = [1,2,3]
# b = (1,2,3)
# a.extend('hi')


# print(a)
print(dir(list))
# print(dir(str))
# print(dir(int))
# print(dir(dict))
# print(dir(set))
# print(dir(tuple))

# words = ["hello", "world", "!"]
# sentence = " ".join(words)
# print(sentence)

count = 0 
number = input() 
if number.isdigit(): 
    number = int(number) 
    count = count+number 
    print(count)

#6
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for i in nums:
#     if i < 5:
#         res.append(i)
# print(res)


#7
# list_ = input().split(",") 
# tuple_ = tuple(list_) 
# print(list_) 
# print(tuple_)