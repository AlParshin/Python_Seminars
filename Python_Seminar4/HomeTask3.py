# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


with open('HomeTask3.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split()
    print('Заданная нами в файле последовательность:')
    print(line)
fin = []
for i in line:
    if (i not in fin) and line.count(i) < 2:
        fin.append(i)
print('Список неповторяющихся элементов:')
print(fin)
