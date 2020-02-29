## Класс - это class как на php со своими свойствами и методами.
## Объект - это экземпляр класса

class MyClass:
    name = 'Anton'; # Вот так написанная переменная она public

    def get_name(self): # тут в отличий от php self надо передавать в методы. Как на php self это этот класс
        return self.name; # self обязательный параметр для метода. Этим функция отличается внутри class и называется метод.

    def func(x):
        return x;

x = MyClass(); # создаем как на php или в js, но без 'new'
x.get_name(); # аналог -> на php. Тут идет обращение как на js с точкой
x.new_arg = 10; # как на php добавляем доп свойства
print(x.func(12));
class People:
    name = 'Anton';
    age = 18;
    work = 'Development';

    def get(self):
        return self

    def _working(self): # одно _ как бы означает что этот класс приватен
        self.work = 'SEO';
        
    def set(self, switch = False):
        if switch:
            self.__del(); # Запускаем приватный метод
        
    def __del(self): # две __ повышение уровня приватности. Теперь нельзя снаружи вызвать
        self.work = None;

y = People();
#print(y.get().name);
#print(y.get().age);
#print(y.get().work);
y._working(); # Вот так конечно можно вызвать, но я не думаю что правильно его вызывать если он назначен как приватный
y.set(True) # Тут я запускаю, удаление work del приватного метода
#print(y.get().work);

## Как известно Python язык который ближе в ООП.
## Тут все наши типы данных являются классами (тут почти все является классами)

# Пример наследование класса!
class MyDict(dict): # В отличий от php класс тут работает как функция принимая атрибуты
    def get(self, key, default = 0):
        return dict.get(self, key, default) # тут классу dict(тип данных словарь)
        # передается self(этот класс) и так получается его метод get переопределится
        # на наш get c параметрами

# Полиморфизм - это разное поведение одного и того же метода в разных классах
# Пример сложение 2-х int и 2-х str. В случае int получается мат вычисление.
class A:

    var = 1;
    def go(self):
        print('Go, A!')

    def sumx(self, a = 0, b = 0):
        return a + b;

class B(A): # вот так передавая класс А мы делаем наследование в классе B елементов А 
    
    def go(self, name): #вот такое переопределение метода называется - полиморфизм
        print('Go, {}!'.format(name))

#pa = A();
#print(pa.go());
#print(pa.sumx(1, 2))
#print('----');
#pb = B();
#print(pb.go('12'))
#print(pb.sumx(3, 4))

## Встроенные магические методы в классах
class bn_a:
    def __init__(self, name): # это __constructor как в php
        self.name = name; # тут self.name создает свойства name в классе
        self.new_prop = 12;

bna = bn_a('Vasya');
#print(bna.name)
#print(bna.new_prop)

class bn_b:
    def __str__(self): # аналог __toString в php
        return 'str';

bnb = bn_b();
#print(bnb);

class bn_c:
    def __del__(self): # аналог метода в php который запускается при удалений класса
        return 'Удален';
    
# Тут в отличий от php магических методов огромное количество

import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Rerp({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

m_x = Vector2D(3, 4); # Констрактом опредилил 2 перменных внутри класса
#print(m_x) # вот так вызывается rerp
#print(abs(m_x)) # ложим объект в abs и тогда вызовится метод __abs__
m_y = Vector2D(1, 2);
#print(m_x + m_y) # мат сложение 2-х объектов приводит к действие метод __rerp__
#print(bool(x)) # обращение в тип bool ривотдит к действию метод __bool__
