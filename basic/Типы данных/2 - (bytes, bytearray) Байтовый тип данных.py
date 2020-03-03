## Байты нужны чтоб хранить в нем цифровую инфу: текст, картинка, музыка.
#x = 'Строка'.encode('utf-8'); # в типе str есть метод encode которая переведет строку в БАЙТ тип
#print(x)

#print(bytes('Байт инфо', encoding='utf8')); # bytes функция для работы с байтами
#print('b\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8')) # b - указака что строка байтовая. decode декодирует обратно в строку.

#print(bytes([50, 2]));

#x = 'Байты'.encode('utf-8');
#print(x[4])

## bytearray это массив байтов.
b = bytearray(b'hello world!')
print(b)
