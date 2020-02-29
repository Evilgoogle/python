def hello():
    print('Hello, world!')

def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

#if __name__ == "__main__":
#    print(123)
# Вот это поянть и изучить
