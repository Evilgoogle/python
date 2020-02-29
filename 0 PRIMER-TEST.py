def func():
    pass

print(func())

def x(*arg):
    return arg

print(x(1,2,3, False, 'str', []))

def y(**arg):
    return arg

print(y(deg='good', age=16))
