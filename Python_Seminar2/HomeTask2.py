# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

print('Введите число:')
N = int(input())
out_list = []
for i in range(1, N+1):
    out_list.append(math.factorial(i))
print(out_list)
