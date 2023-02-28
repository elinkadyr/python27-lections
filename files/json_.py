'==========JSON=========='
# JavaScript Object Notation - единый формат, в котором могут храниться только те типы данных которые есть во всех языках программирования поддерживающие json
# int, float
# str
# dict
# bool True False
# list
# type None

import json

# сериализация - перевод из Python в Json
# dump
# dumps - функция которая переводит Python объект в Json строку

# десериализация - перевод из Json в Python
# load
# loads - функция которая переводит Json строку в Python объект

# print(dir(json))

python_list = [1,2,3]
json_list = json.dumps(python_list)
print(type(python_list))        #list    [1,2,3]
print(type(json_list))          #str    '[1,2,3]'

json_dict = '{"a":1, "b":2}'
python_dict = json.loads(json_dict)
print(type(json_dict))          #str    #{"a":1, "b":2}
print(type(python_dict))        #dict   #{'a': 1, 'b': 2}

list_ = [
    1,2,3,
    4.5,
    (1,2,3),
    {'a':1},
    'hello',
    True, False, None
]
with open ("test.json", "w") as file:
    json.dump(list_, file)

with open ("test.json", "r") as file:
    res = json.load(file)

print(res)  #[1, 2, 3, 4.5, [1, 2, 3], {'a': 1}, 'hello', True, False, None]