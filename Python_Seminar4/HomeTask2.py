# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.


with open('HomeTask2.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split()
    n = int(line[0])
    print('Наше число из файла =', n)
a = []
d = 2
while d * d <= n:
    if n % d == 0:
        a.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    a.append(n)
if len(a) == 1:
    print('Наше число является простым числом!')
else:
    print('Простые множители числа N =', a)
