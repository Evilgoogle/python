## функций - объект принимающей аргументы и вохвращаюшей значений
## создается с помощью def
def plus(x, y):
    return x + y
#print(plus('doom', 'guy')); 

x = plus(1, 2);
#print(x)

# если функция не делает return, то он возвращяет объект none (аналог null в js)
def func():
    pass
#print(func())

def foot(a, b, c=2): # как и на php параметр по умолчанию с=2
    return a + b + c
#print(foot(1,2,3))
#print(foot(1,4))
#print(foot(a=1, c=4, b=0)) # опеределяем свой порядок передачи аргументов
#print(foot(c=0, a=0, b=1)) # опеределяем свой порядок передачи аргументов

def primer(*arg):
    return arg
#print(primer(1, 2, 3, False, 'str'))
# во функцию можно передавать любое кол-во аргументов, но для этого надо
# поставить знак * - primer(*args). Эти входящие аргументы python положит
# в кортеж (1, 2, 3, False, 'str')

def funkdict(**args):
    return args
#print(funkdict(v_int=1, v_str='str', v_bool=False))
# Если мы хотим аргументы пришли как словарь, тогда вставим ** и передаем так a=1
# {'v_int': 1, 'v_str': 'str', 'v_bool': False}

## Анониные функций - lambda. Они быстрее работают в отличий от функций и возвращяет без return
print((lambda x,y: x + y)(1, 2)) # думаю он подходит для мелких задач типа тернарных операторов
