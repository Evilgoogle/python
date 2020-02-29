## while - в теле цикла имеется условье. Если она истина циклы выполняется
#i = 100;
#while i > 2:
#    print(i)
#    i = i-1
#x = 0
#while x < 5:
#    x += 1
#    print(x)
#else: 
#    print('Завершен');

## for - это аналог for в js. Похож на foreach в php. Он нужен для перебора объектов.
#for i in 'hi good'
#    print(i);

#for x in 'hello world':
#    if x == 'l':
#        continue # пропускает этот ход. Идет следующяя итереация
#    print(x)

# for y in 'hello world':
#   if y == 'o':
#        break # останавливает цикл в этом момента. Далбше итераций не идут
#    print(y);

#x = 'hello word';
#x = [1,2,3,4];
#x = {'name': 'Anton', 'age': 18}

#for v in x: # как то похож на js
#    print(v) # но тут отдает как php, а не x[v] в js

x = 'hello word';
x = [1,2,3,4];
x = {'name': 'Anton', 'age': 18}
x = [
    {'name': 'Anton', 'age': 18},
    {'name': 'Anna', 'age': 14}
]

for v in x:
    print(v['name'])
