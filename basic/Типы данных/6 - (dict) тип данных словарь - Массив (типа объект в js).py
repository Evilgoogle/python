## Тип данных dict - это массив, как ассоцативный массив или объект в js
## Она состоит из ключа и значение

#d = {}; # создал пустой массив. Массив можно создовать как на php
#print(d)
#print(type(d))

#s = {'name': 'Anton', 'age': 18} # создаю как на php
#print(s);
#print(s['name']) # вызов как на php

#x = dict(name='Anton', age=18); # создать с помощью dict
#print(x['name'])
#d = dict.fromkeys([a, b], 100); # через fromkeys метод dict
# Можно создать через генератор словарей

#a = {0: 1, 1: 2, 2: 4}
#print(a[0]) # вытаскиваем
#a[5] = 'good'; # расшираем словарь
#a[1] = 'Tech'; # перезаписываем
#print(a);

# Для работы со словарями используем dict. Он дает возможность очищать,
# копировать, удалять и так далее
name = {'name': 'Anton', 'age': 18}
#dict.clear(name); # очищение
#ftor = dict.copy(name) # копируем
#name['name'] = 'Allan'
#print(name)
#print(ftor)
#print(dict.keys(name)) # получаем ключи
#так далее
