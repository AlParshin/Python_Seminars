# Напишите программу, удаляющую из текста все слова, содержащие буквы "а" "б" или "в".


with open('HomeTask1_start.txt', 'r', encoding='utf-8') as file:
    statya = file.read()
    file.close()
statya.replace('\n', '')
statya = list(statya.split())
print('Исходный текст (списком элементов):')
print(statya)

final = []
for i in statya:
    # if ('а' and 'А' and 'б' and 'Б' and 'в' and 'В') not in i:
    if ('а' not in i) and ('б' not in i) and ('в' not in i) and ('А' not in i) and ('Б' not in i) and ('В' not in i):
        final.append(i)
print('----------------------------------------------------------------------------------------------------------------------------------------------')
print('Конечный текст:')
print(" ".join(map(str, final)))

finish = list(map(str, final))

with open('HomeTask1_finish.txt', 'w', encoding='utf-8') as file:
    for i in finish:
        file.write(i + '\n')
    file.close()
