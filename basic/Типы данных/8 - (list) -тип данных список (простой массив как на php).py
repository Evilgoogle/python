# list - массив на подобие простых массивов в php. Точно так же нумеруется 0,1,2,..n
a = list('list') # функ list оздает списки
b = []; # вот так создаем пустой список
c = ['a', 'b'] # создаем с данными
#print(a, b, c)

x = [1, 'good', False, [1,2], {'name': 'Anton'}, 45.04, {'a', 2}];
#print(type(x[0]), type(x[1]), type(x[2]), type(x[3]), type(x[4]), type(x[5]), type(x[6]))
#print(type(x))

## Функий для типа list ##
#c.append(48); # добавляем елемент в конце
#print(c)

#c.extend(x) # добавляем содержимое списка x в конец списка c. Это аналогия array_merge
#print(c)

#c.insert(1, 'str') # добавляем после ключа 1 значение str
#print(c) # ['a', 'str', 'b']

#c.remove('b'); # удаляем значений. В данном случае b
#print(c)

#w = c.pop(1) # удаляем значение b и передаем его в переменную
#print(w)
#print(c)

#ro = x.index(False, 0, 10) # ищет. Если не находит вернет ERROR, если найдет то индекс

# Далее есть такие же функций для работы со списками

## Получаем елементы из списка ##
## получаем по индексу
#print(x[2]) # обращаемся на индекс и получаем значение
#print(x[-1]) # можно брать с обратной стороны с отрицательными индексами
## получаем по срезам (start:stop)
#print(x[:]) # получаем весь массив (без среза). Пустой _:_ означает 0:0
#print(x[1:]) # срезаем 1 и получаем остальное
#print(x[:2]) # от 0 до 2 - [1, 'good']
#print(x[1:3])
#print(x[:-2])
