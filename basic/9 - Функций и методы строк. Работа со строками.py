## Функций и методы строк
# Как известно строки это тип str. А str это класс со своими методами

# Сложение
s1 = 'span';
s2 = 'root';
print(s1 + s2);

# Дублирование
print('span' * 3);

# Вычет длины строки через функцию len
print(len('span'));

# Получаем по индексу
s = 'good';
print(s[0], s[3]); # Получаю символы. Строка ведет себя как ммассив
print(s[0:2]);

# Другие методы строк
print(r'C:\temp\new')# r - подавляет знак экранирование
print(b'byte')
print(s.find('g')) # ищем и находим букву g (1|-1)
print(s.replace('d', 't'))
# так далее

## метод format для форматирвания строки
g = '{0}, {1}, {2}'.format('a', 'b', 'c');
g = '{2}, {0}, {1}'.format('a', 'b', 'c');
g = '{0}, {1}, {2}'.format(*'who');
g = 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
print(g)
