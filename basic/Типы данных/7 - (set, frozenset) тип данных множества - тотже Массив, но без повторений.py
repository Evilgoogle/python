## Множества - это массив данных как list, c отличием что у нее нет повторений и она их составляет с определным порядком
## Если найдутся повторений, то они сотрутся.
## Множества есть 2 вида: set и frozenset

## SET
a = set('hello'); # вот так создается массив set
#print(type(a))
#print(a)

b = {'a', 'b', 'c', 'd', 'e'} # она может создаватся так, типа как dict
#print(type(b))
#print(b)

c = {} # вот так set не создается, так как он не может быть пустым. Тут будет dict
#print(type(c))
#print(c)

x = {'name': 'Anton', 'age': 18, 'h': [1,2]} # dict

f = set('hello');

#print(len(a)) # функ len(a) считает кол-во елементов в массивах (dict, set)
#print('h' in a) # x in a - так мы ищем наличие значение в set массивах, а в dict ищем такой ключь. Возврщяет true или false
#print(a.isdisjoint(b)) # метод isdisjoint ищет обшие елементы в двух массивах - set1.isdisjoint(set2|dict). Пример я ищу совпадений в set и в dict массиве -#print(a.isdisjoint(x)). Есть ли есть совподение - False
#(a == f); # проверяем одинаковость массивов.
#print(a.union(b)) # обядинит множества.
#a.copy(b) # копирование множеств
# далее много много функция для работы: pop, clear, add, remove и так далее

## FROZENSET - это тот же set, но его нельзя изминить после создание.
