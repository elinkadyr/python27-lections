"===============Циклы==============="
#цикл - блок кода, который отрабатывается несколько раз
#for - цикл, который работает с итерируемыми объектами, цикл закан.ет свою работу когда он доходит до последнего элемента в итерируемом объекте 
#while - цикл, который работает до тех пор, пока условие верное

list1 = ['hello', 10, True, [1,2,3]]
for element in list1:
    print(element)

string1= 'Hello world'
for letter in string1:
    print(letter)
#CTRL + C ЧТОБЫ ОСТАНОВИТЬ

i = 1
while i != 10:
    print('hello', i)
    i = i + 1
 
i = 0
while i:
    print('Hello world')
    i = i + 1 #вообще не отработает потому что 0 = false

"================Ключевые слова в циклах================"
#break - полностью останавливает цикл
#continue - переход к след. итерации

for i in range(10):
    if i == 3:
        break
    print(i)        


for i in range(10):
    if i == 3:
        continue
    print(i)

for i in range(10):
    print(i)
    break
#0

list2 = [1,2,3,4,3,4,3,1,1,]
for x in list2:
    if 1 in list2:
         list2.remove(1)
print(list2)

list2 = [1,2,3,4,3,4,3,1,1]
while 1 in list2:
    list2.remove(1)
print(list2)