class Person:
    arms = 2
    legs = 2
    name = 'Elina'

    def __init__(self, name):
        # __init__ - dunder метод, который добавляет в объект self аттрибуты, которые отличаются у рахных объектов
        self.name = name

    def walk(self):
        #self - ссылка на объект, у которого мы вызываем данный объект
        print(self)
        print("я хожу")

# person1 = Person()
# print(person1)          # <__main__.Person object at 0x7effa835baf0>
# print(type(person1))    # <class '__main__.Person'>

# print(person1.walk())
# Person.walk(person1)
# person1.walk()

# p1 = Person()
# p2 = Person()
# p3 = Person()
# # print(p1.name, p2.name, p3.name)

# print(dir(Person))

person1 = Person('Elina')
person2 = Person('Elle')
print(person1.name, person2.name)


# Аттрибут класса и аттрибуты объекта класса 

class A:
    var1 = "переменная класса"

    def __init__(self):
        self.var2 = "переменная объекта"

print(dir(A))
