# Полиморфизм 
> принцип ООП, в котором метожы в разны классах называются одинаково (один интерфейс, разный функционал)

```py
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
```