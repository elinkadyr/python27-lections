class Dog:
    def speak(self):
        print(("гав-гав"))

class Cat:
    def speak(self):
        print(("мяу-мяу"))

class Frog:
    def speak(self):
        print(("ква-ква"))

animals = [Cat(), Dog(), Frog(), Cat(), Dog(), Frog()]
for animal in animals:
    animal.speak()

# __add__

a = 4 
b = 5
print(a.__add__(b))
print(a+b)

a = [1,2,3]
b = [4,5,6]
print(a.__add__(b))


# __len__
a = 'abc'
print(len(a))
print(a.__len__())

b = [1,2,3,[4,5,6]]
print(len(b))
print(b.__len__())
