"Миксины"
# классы, которые будут использоваться для наследования 
# но от миксинов не создаются объекты

# классы - примеси, которые служат для расширения функционла класса
# от миксинов нельзя создавать объекты, поскольку миксины - не самостоятельные классы 
# при наследовании миксины должны идти в первую очередь


class WalkMixin():
    def walk(self):
        print('i can walk')

class SwimMixin():
    def swim(self):
        print('i can swim')

class FlyMixin():
    def fly(self):
        print('i can fly')

class Human(WalkMixin, SwimMixin):
    name = 'Tom Hardy'

    def talk(self):
        print('i can talk')

class Fish(SwimMixin):
    name = 'Dora'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'Alvin'

class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'Tweety'



# objects = [Human(), Fish(), Exocoetidae(), Duck()]

# for obj in objects:
#     # print(obj.name)

#     attrs = ['fly', 'swim', 'walk', 'talk']
#     for attr in attrs:
#         if hasattr(obj, attr):
#             method = getattr(obj, attr)
#             method()



obj = Human()
# print(hasattr(obj, 'fly'))      # False
# print(getattr(obj, 'walk') )    # <bound method WalkMixin.walk of <__main__.Human object at 0x7f237db57d90>>
# method = getattr(obj, 'walk')   # i can walk
# method()
# setattr(obj, 'new_attr', 'hello world')
# # print(dir(obj))
# print(obj.new_attr)

# hassatr - функция принимает объект и название аттрибута. Возвращает TRUE, если у объекта есть такой аттрибут (метод)
# getattr - функция принимает объект и название аттрибута. Возвращает значение аттрибута
# setattr - функция принимает объект и название аттрибута и значение аттрибута. Добавляет в объект  новый аттрибут или перезапишет одноименный аттрибут 

