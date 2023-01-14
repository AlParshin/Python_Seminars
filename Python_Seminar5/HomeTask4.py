# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Алгоритм RLE (англ. Run-Length Encoding) — алгоритм сжатия, заменяющий ИДУЩИЕ ПОДРЯД одинаковые символы парой (повторяющийся символ, количество повторений).
# Например, строчку aaababbcbbb он переводит в (a, 3) (b, 1) (a, 1) (b, 2) (c, 1) (b, 3).

print('Введите строку английских букв:')
spisok = list(input())
print(spisok)

count = 1

count_list = []
character_list = []

for i in range(1, len(spisok)):
    if spisok[i] == spisok[i-1]:
        count += 1
    else:
        count_list.append(count)
        character_list.append(spisok[i-1])
        count = 1
    if i == len(spisok)-1:
        count_list.append(count)
        character_list.append(spisok[i])

print('Результат RLE алгоритма:')
print(list(zip(character_list, count_list)))
