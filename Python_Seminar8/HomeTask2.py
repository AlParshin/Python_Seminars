# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром Цезаря и возвращает его.
# Шифр Цезаря заменяет каждую букву в тексте на букву, которая отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита.
# Если сдвиг не указан, то пусть ваша функция кодирует сдвиг алфавита на 3 позиции:
# А→Г, А→Г,
# Б→Д, Б→Д,
# В→Е, В→Е,
# ……
# Э→А, Э→А,
# Ю→Б, Ю→Б,
# Я→В, Я→В
# Все символы, кроме русских букв должны остаться неизменными.
# Маленькие буквы должны превращаться в маленькие, большие — в большие.
# Напишите также функцию декодирования decrypt_caesar(msg, shift), также использующую сдвиг по умолчанию.
# При написании функции декодирования используйте вашу функцию кодирования.

def encrypt_caesar(msg, shift):
    new = ''
    for i in range(len(msg)):
        if msg[i].isalpha() == True:
            temp = ord(msg[i]) + int(shift)
            new += chr(temp)
        else:
            new += msg[i]
    return new


def decrypt_caesar(msg, shift):
    new = ''
    for i in range(len(msg)):
        if msg[i].isalpha() == True:
            temp = ord(msg[i]) - int(shift)
            new += chr(temp)
        else:
            new += msg[i]
    return new


msg = input('Введите любой текст на русском языке: ')
shift = input('Введите сдвиг алфавита: ')
if shift == '':
    shift = 3

msg = encrypt_caesar(msg, shift)
print(msg)
msg = decrypt_caesar(msg, shift)
print(msg)
