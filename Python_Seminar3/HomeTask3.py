# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('Введите количество элементов списка:')
a = []
kolvo = int(input())
for i in range(kolvo):
    print('Введите элемент с индексом', i)
    a.append(float(input()))
print('Получился вот такой список:')
print(a)
minim = 1000000000
maxim = 0
for i in range(kolvo):
    # если число целое (без дробной части), то оно в моем решении не учитывается, как минимальное (хоть и дробная часть = 0)
    # в приведенном в условии примере было целое число "5", но оно также не учитывалось как минимальное
    if 0 < a[i] % 1 < minim:
        minim = a[i] % 1
    if a[i] % 1 > maxim:
        maxim = a[i] % 1
print('Иокомая разница равна:', round(maxim-minim, 2))
