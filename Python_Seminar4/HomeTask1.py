# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
with open('HomeTask1.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split()
    d = float(line[0])
    print('Заданная нами в файле точность = ', d)
    d = str(d)
    for i in range(len(d)):
        if d[i] == '1':
            tochn = i-1
    pi = math.pi
    print(pi)
    print('Число Пи с заданной нами точностью = ', round(pi, tochn))
