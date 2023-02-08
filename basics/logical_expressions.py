"=======Логические выражения======="
'= знак присвоения'
'== знак сравнения'
# print (5 == 5)  -> true
# print (5 == 4)  -> false
'!=    знак неравенства'
# print(4 != 5)      -> true
# print(4 != 4)      -> false
'знак больше >'
#print(5 > 5)       -> false
#print(5 > 4)       -> true
'знак меньше <'
#print(5 < 4)       -> false
#print(5 < 10)      -> true
'больше или равно >='
#print(5>=10)       -> false
#print(5>=5)        -> true
'меньше или равно <='
#print(5<=3)                    -> false
#print(5<=5)                    -> true
#print('5'=5)                   ->false
#print('hello'=='hello')        ->true
#print('Hello'=='hello')        ->false

"=========AND OR NOT========="
#and и
#or или 
#not не

a = 5
b = 6
#print(a==5 and b==6)           ->true
#print(a==4 and b==5)           ->false
#print(a==4 or b==3)            ->false
#print(a==3 or b==3)            ->true
#print(not a==5)                ->false
#print(not a==3 and not b==6)   ->false
#print(not a==3 or not b==6)    ->true
#print(not True)                ->false
#print(not False)               ->true

"========== Boolean Type =========="
#У булевого типа всего 2 значения: True, False
#print(bool(1))          ->true
#print(bool(10))         ->false
#print(bool(-11))        ->true
#print(bool('hello'))    ->true
#print(bool(' '))        ->true
#print(bool(''))         ->false
#print(bool([])          ->false
#print(bool([[]]))         ->true

"========== NON TYPE =========="

# none - неизменяемый тип данных с одним значением none, который используется для обозгачения пустоты
#print(bool(None))         ->false
#print(bool('None'))        ->true

#УСЛОВНЫЕ ОПЕРАТОРЫ -конструкция которая используется для того, чтобы при входных данных код работал по-разному, в зависимости от условия

#if условие1:
    #тело1  
    #тело1 будет выполняться только если условие1 верно

#if условие1:
    #тело1
    #тело1 будет выполняться только если условие1 верно
#else
    #тело2
    #тело2 будет выполняться во всех других условиях


#if условие1:
    #тело1
    #тело1 будет выполняться только если условие1 верно
#elif условие2:
    #тело2:
    #тело2 будет выполняться только если
    #условие1 не верное и если условие2 верное

#if условие1:
    #тело1 
    #тело1 будет выполняться только если условие1 верно
#elif условие2:
    #тело2:
    #тело2 будет выполняться только если
    #условие1 не верное и если условие2 верное
#else:
    #тело3 будет выполняться во всех других случаяx

#В одной конструкции мы можем использовать только один if
#В одной конструкции мы можем использовать неограниченное количество elif или не использовать его вообще
#В одной конструкции мы можем использовать только один else или не использовать его вообще

#num = int(input('Введите число: '))
#if num > 0: 
    #print(f'число {num} - положительное')

#num = int(input('Введите число: '))
#if num > 0: 
    #print(f'число {num} - положительное')
#elif num==0:
    #print(f'число {num} - это 0')
#else:
    #print(f'число {num} - отрицательное')

# password = input('Придумайте свой пароль: ')
# first_let = password[0].upper()
# print(first_let)
# if len(password) >= 8:
#     print("Ваш пароль меньше 8 символов")
# elif not password.startswith(first_let.upper()):
#     print('Ваш пароль не начинается с большой буквы')
# else:
#     print('Успешно создан пароль')

"=====Тернарные операторы====="
#тернарные операторы - условие в одну строку
#тело1 if условие else тело2

# num = int(input())
# res = 'Hello' if num == 5 else 'Bye'
# print(res)

'==========FizzBuzz=========='
# num = int(input('Введите число: '))
# if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')

# else:
#     print(num)

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

