class CreateMixin:
    def product_create(self, title, price):
        # self.__class__ - обращение к классу который наследовался от этого миксина
        model = self.__class__
        obj = model()
        _id = model._id
        obj.title = title
        obj.price = price
        obj.id = _id
        model.objects[_id] = obj
        model._id += 1

class ReadMixin:
    def product_detail(self, p_id):
        model = self.__class__
        obj = model.objects.get(p_id)
        print({"id": obj.id, "title": obj.title, "price": obj.price})

class UpdateMixin:
    def product_update(self, p_id, title, price):
        model = self.__class__
        obj = model.objects.get(p_id)
        obj.title = title
        obj.price = price

class DeleteMixin:
    def delete_product(self, p_id):
        model = self.__class__
        model.objects.pop(p_id)

class ProductCrud(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    objects = {}
    _id = 1


# crud = ProductCrud()
# crud.product_create('Pizza', 420)
# crud.product_create('Lasagna', 300)
# crud.product_detail(1)
# # crud.product_detail(2)
# crud.delete_product(2)
# crud.product_detail(2)

# crud.product_detail(2)
# crud.product_update(2,'Lasagna', 350)
# crud.product_detail(2)

"1"
# class Auto:
#     def ride(self):
#         print("Riding on a ground")

# class Boat:
#     def swim(self):
#         print("Floating on water")
    
# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# obj.ride() 
# obj.swim() 

"2"
# class RadioMixin:
#     def play_music(self, title):
#         self.title = title
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     def ride(self):
#         print("Riding on a ground")

# class Boat(RadioMixin):
#     def swim(self):
#         print("Floating on water")
    
# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music('pizaa')
# boat.play_music('lasagna')
# obj.play_music('pasta')

"3"
class Clock:
    def current_time(self):
        print('13:30:00')
    
class Alarm:
    def on(self):
        print('08:00:00')
    def off(self):
        print('08:10:00')

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        print('Будильник включен')

clock = AlarmClock()
clock.current_time() 
clock.alarm_on() 

import datetime 
class Clock: 
    def current_time(self): 
        dt_now = datetime.datetime.today().strftime("%H:%M:%S") 
        print(dt_now) 

class Alarm: 
    @staticmethod 
    def on(): 
        print('Будильник включен') 
        
    @staticmethod 
    def off(): 
        print('Будильник выключен') 

class AlarmClock(Clock, Alarm): 
    @staticmethod 
    def alarm_on(): 
        Alarm.on() 
        
clock = AlarmClock() 
clock.current_time() 
clock.alarm_on()