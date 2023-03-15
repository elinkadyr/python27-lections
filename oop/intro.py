# class Person:
#     arms = 2
#     legs = 2
#     name = 'Elina'

#     def __init__(self, name):
#         # __init__ - dunder метод, который добавляет в объект self аттрибуты, которые отличаются у рахных объектов
#         self.name = name

#     def walk(self):
#         #self - ссылка на объект, у которого мы вызываем данный объект
#         print(self)
#         print("я хожу")

# # person1 = Person()
# # print(person1)          # <__main__.Person object at 0x7effa835baf0>
# # print(type(person1))    # <class '__main__.Person'>

# # print(person1.walk())
# # Person.walk(person1)
# # person1.walk()

# # p1 = Person()
# # p2 = Person()
# # p3 = Person()
# # # print(p1.name, p2.name, p3.name)

# # print(dir(Person))

# person1 = Person('Elina')
# person2 = Person('Elle')
# print(person1.name, person2.name)


# # Аттрибут класса и аттрибуты объекта класса 

# class A:
#     var1 = "переменная класса"

#     def __init__(self):
#         self.var2 = "переменная объекта"

# print(dir(A))

"==================Введение в ООП=================="
"1"
# class Song:
#     def __init__(self, title, author, year): 
#         self.title = title 
#         self.author = author 
#         self.year = year 
#     def show_title(self): 
#         return f"Название этой песни {self.title}"
#     def show_author(self): 
#         return f"Автор этой песни {self.author}"
#     def show_year(self): 
#         return f"Эта песня вышла в {self.year} году"

# song = Song("Happy", "Pharrell Williams", 2013) 
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())
"2"
# class Circle:
#     color = "Синий"
#     pi = 3.14 

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         result = self.pi * self.radius ** 2
#         return(result)

# circle = Circle(2)
# circle.color = "red"
# print(circle.color)
# print(circle.get_area())

"3"
# class BankAccount:
#     def __init__(self): 
#        self.balance = 0 
    
#     def withdraw(self, amount): 
#        self.balance -= amount
#        return f"Ваш баланс {self.balance} сом"
    
#     def deposit(self, amount): 
#        self.balance += amount
#        return f"Ваш баланс {self.balance} сом"

# account = BankAccount()
# print(account.withdraw(12))
# print(account.deposit(1000))

# class BankAccount:
#     balance = 0
    
#     def withdraw(self, amount): 
#        self.balance -= amount
#        print(f"Ваш баланс {self.balance} сом")
    
#     def deposit(self, amount): 
#        self.balance += amount
#        print(f"Ваш баланс {self.balance} сом")

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

"4"
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.cost = self.cost_km * km + self.cost 
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом' 

# taxi1 = Taxi('Namba',50,10)
# taxi2 = Taxi('Yandex',50,10)
# taxi3 = Taxi('Jorgo',50,10)

# print(taxi1.get_total_cost(15)) 
# print(taxi2.get_total_cost(12)) 
# print(taxi3.get_total_cost(14))  

"5"
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
    
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('El','Ka',108875)
# contact.get_info()

"6"
# class Salary:
#     percent = 8 
#     def __init__(self, salary, experience): 
#         self.salary = salary 
#         self.experience = experience 
    
#     def count_percent(self): 
#         return self.salary * (self.percent / 100) * self.experience 
    
# obj = Salary(14566, 12) 
# print(obj.count_percent())
"7"
# import datetime 
# class Nobel(): 
#     def __init__(self, category, year, winner) -> None: 
#         self.category = category 
#         self.year = year 
#         self.winner = winner 
#     def get_year(self): 
#         a = datetime.datetime.now() 
#         res = a.year - self.year 
#         return f'выиграл {res} лет назад' 
    
# winner1 = Nobel("Литература", 1945, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year()) 
# # winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# # print(winner2.category, winner2.year, winner2.winner) 
# # print(winner2.get_year()) 

"8"
# class Password: 
#     def __init__(self, password): 
#         self.password = password 

#     def __str__(self):
#         return '*' * len(self.password) 
    
#     def validate(self): 
#         if not len(self.password) >= 8 and len(self.password) < 15: 
#             return f'Password should be longer than 8, and less than 15'
        
#         if not any(map(lambda i: i.isdigit(), self.password)): 
#             return f'Password should contain numbers too' 
        
#         if not any(map(lambda i: i.isalpha(), self.password)): 
#             return f'Password should contain letters as well' 
        
#         if not any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)): 
#             return f'Your password should have some symbols' 
        
#         return f'Ваш пароль сохранен.' 

# password = Password('1ell444e@') 
# print(password.validate()) 
# print(password)

"9"
# class Math: 
#     def __init__(self, number): 
#         self.number = number 

#     def get_factorial(self): 
#         self.factorial = 1 
#         for i in range(2, self.number+1): 
#             self.factorial = self.factorial * i 
#             return self.factorial 
    
#     def get_sum(self): 
#         number = [int(x) for x in str(self.number)] 
#         suma = sum(number) 
#         return suma 
    
#     def get_mul_table(self): 
#         s = '' 
#         for i in range(10): 
#             s += f'{self.number} * {i+1} = {self.number * (i+1)}' + '\n' 
#         return s 
    
# a = Math(0) 
# print(a.get_factorial())
# print(a.get_sum()) 
# print(a.get_mul_table())

"10"
class ToDo: 
    def __init__(self,string): 
        self.todo = string 
    instances = dict() 
    def give_priority(self,priority): 
        ToDo.instances[priority]=self.todo 
    def list_of_tasks(self): 
        return sorted(ToDo.instances.items()) 
var1=ToDo('ckelele') 
var1.give_priority(2) 
var2=ToDo('lelelele') 
var2.give_priority(3) 
var3=ToDo('HIOHOHO') 
var3.give_priority(1) 
print(var3.list_of_tasks())


"================Наследование================"
"1"
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass

# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

"2"
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

    
# obj = B()
# obj.method1()

"3"
# class MyString(str):
#     def __init__(self, stroka1): 
#         self.stroka1 = stroka1 
#     def append(self, stroka2): 
#         self.stroka2 = stroka2 
#         self.stroka1 = self.stroka1 + self.stroka2 
#         return self.stroka1 
#     def pop(self): 
#         last_elem = self.stroka1[-1] 
#         self.stroka1 = self.stroka1[:-1] 
#         return last_elem
#     def __str__(self) -> str: 
#         return self.stroka1 

# example = MyString('String') 
# example.append('hello') 
# print(example.pop()) 
# print(example)
# el = 'elina'
# last_elem = el[-1] 
# el = el[:-1]
# print(last_elem, el)
"4"

# print(a.get_mul_table())
"5"
# class Person: 
#     def __init__(self,name, age): 
#         self.name = name 
#         self.age = age 

#     def display(self): 
#         return f'name:{self.name}, age:{self.age}'
     
# class Student(Person): 
#     def __init__(self, name, age, faculty): 
#         super().__init__(name, age) 
#         self.faculty = faculty 
        
#     def display_student(self): 
#         info = super().display() 
#         info += f', faculty:{self.faculty}' 
#         return info
        
# obj_student = Student('El', 21, 'IT') 
# print(obj_student.display()) 
# print(obj_student.display_student())
