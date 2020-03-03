## try - except - это тип данных в Python для обработки исключений
## Этот работает также как в php, но он модет отлавливать ошибки в отличий от php

#10/0
# Отдает ошибку в исключений ZeroDivisionError
# Здесь указан File в каком файле и в какой строке произошда ошибка
# Вот этот ZeroDivisionError можно отловить с try except

#2 + '1'
#Отдает TypeError 

#int('str')
#Отдает ValueError

try:
    k = 10 / 0;
except ZeroDivisionError:
    print('На ноль делить нельзя. Вот получи к');
    k = 0
print(k)

try:
    a = 1 + 'str';
except TypeError:
    print('Нельзя сложить int тип со str типом');
    a = 'None'
print(a)    

try:
    int('str')
except  ValueError:
    print('Нельзя преоброзовать строки в integer');

## Есть не обязательные парметры:
#else - которая срабатывает если исключений нет
#finally - этот срабатыает в любом случае вне зависмости есть исключние или нет.

file = open('newfile', 'r')
