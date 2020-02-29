## ----> Экранирование строк
## Можно писать с ' или " тут разницы нет.
# x = 'name';

## Сырые строки - помагает подавить знак \ если он имеется в тексте.
#x = 'C:\newt.txt'; # Здесь есть спец символ \n  из за него текст перейдет в новый абзац.
#y = r'C:\newt.txt'; # Здесь вставляю r и \n заигнорится 
#print(y);
#s = r'\n\n\\'[:-1];
#print(s);

## Для байтовых строк есть b
#fx = b'byte'

## Вставка 3-x ''' поммагет игнорить в тексте "" '' кавычки. Только в тексте не должно быть ''' кавычки
#c = '''это очень большая  тут написано - "HighLoad" или 'Большая нагрузка'
#... строка, многострочный
#... блок текста''';
#print(c);

##-------------------------##
## ----> Работаем со строками
# Сложение строк
#s1 = 'snap'
#s2 = 'exp'
#print(s1 + s2); ## результат: snapexp

# Дублирование строк (умножение)
#print('span-' * 3, end='span'); ## результат: span-span-span-span

## Функция len - проверка длины строки
#x = len('good')
#print(x);

## обращаемся и получучаем символ по индексу
#r = 'what is my water?'
#print(r[3]); #результат: t
#print(r[9]); #результат: y
#print(r[-1]); #результат: ?
#print(r[2:7]) #обрезаем с 2 строки до 7э ||at is 
#print(r[0:-1]) # what is my water

## find - поиск в строке. Возвращает индекс строки, при false возваращает -1
#x = 'what is my water?';
#print(x.find('a', 0, 7)); # rfind -работает наборот с последней строки ищет.

## replace - замена
#x = 'what is my water?';
#print(x.replace('water', 'cat')); # what is my cat?

## split - разбиение строки 
#x = 'what is my water?';
#print(x.split('a')); # ['wh', 't is my w', 'ter?']

## Разные виды проверок является ли isdigit, isalpha, isalnum,islower, isupper
#x = 'water';
#print(x.isalpha()); # true
#print(x.isdigit()); # false

## Дальше таких функий для работы со строками https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

## Форматирование строки ##
## есть метод format или %
print('Hello, {}'.format('Vasya')) #Hello, Vasya
print('word: {}, {}, {}'.format('a', 'b', 'c')) #word: a, b, c
print('word: {2}, {0}, {1}'.format('a', 'b', 'c')) #word: c, a, b. Тут по индексу определяем какой символ где будет стоять {2}
print('word: {2}, {0}, {0}'.format('a', 'b', 'c')) #word: c, a, a. C индексами точно определяем что вставить
print('word: {}, {}, {}'.format(*'word')) # знак * - позволяет вставить текст и получать от него буквы по индексу
print('Coordinates: {lat}, {lng}'.format(lat='48.8', lng='94.76')) #Coordinates: 48.8, 94.76
coord = {'lat': 48.8, 'lng': 94.76}
print('Coordinates: {lat}, {lng}'.format(**coord)) # знак ** - позволяет вставить значениий из словаря 
print('Coordinates: {coor[0]!r}, {coor[1]!r}'.format(coor = ['48.8', '94.76']))
# Дальше есть много возможности работы со строками
