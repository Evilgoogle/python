## int - числовой тип данных в python. Тут как на php с этим типом можно провести арифметические операций
#x = 86
#print(x);

#x = int(86.868) # функция int преоброзует в int в числовой тип
#print(x);

## Над целыми числами можно проводить битовые операций
# У типа int есть след методы для работы с битами
x = 12 
print(x.to_bytes(2, byteorder='big')) # метод to_bytes переводит int в формат байтов 
print(int.from_bytes(b'\x00\x0c', byteorder='big')) # переводим обратно
