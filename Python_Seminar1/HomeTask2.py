# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

print('Введите координаты X:')
X = int(input())
while X == 0:
    print('Введите другую координату X, не равную 0 !!!')
    X = int(input())
print('Введите координаты Y:')
Y = int(input())
while Y == 0:
    print('Введите другую координату Y, не равную 0 !!!')
    Y = int(input())
if X > 0 and Y > 0:
    print('1 четверть')
elif X < 0 and Y > 0:
    print('2 четверть')
elif X < 0 and Y < 0:
    print('3 четверть')
elif X > 0 and Y < 0:
    print('4 четверть')
