## В python есть подключение модулей типа как в js
## import 'name'. Любая написанная нами страница может стать модулем 
## После импотра название модуля становится переменной как в js
import math as m # as аналог как в mysql
#print(m.pi)

from math import ceil as c #, e, 'n' колво атрибутов. # Импортируем определнные атрибуты от модуля
from math import (sin, cos, tan, atan) # импортируем определенные атрибуты
from math import * # импортироватть все атрибуты

## Пишем свои модуль. # пути на модуль каззывается в перменной sys.path
import primer

print(primer.hello());
print(primer.fib(11))
