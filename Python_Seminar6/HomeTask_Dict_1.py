# 1. Фрукты
# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество.
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение. Например:
# Ввод:
# >> 3 # Количество фруктов
# >> Яблоко
# >> 3
# >> Апельсин
# >> 3
# >> Мандарин
# >> 10
# Вывод:
# >> {'Яблоко': 3, 'Апельсин': 3, 'Мандарин': 10}

print("Введите количество фруктов:")
i = int(input())
fruits = dict([input('Введите ключ и значение через пробел:').split()
              for _ in range(i)])
print(fruits)