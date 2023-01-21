# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.
# Ввод:
# >> 3 # Количество друзей
# >> Иван
# >> 11
# >> Саша
# >> 12
# >> Леша
# >> 10
# Вывод:
# >> Леша

print("Введите количество друзей:")
i = int(input())

friends = []
ages = []

for _ in range(i):
    friends.append(
        dict([input('Введите ключ и значение через пробел:').split()]))
print(friends)

for j in range(i):
    for k, v in friends[j].items():
        ages.append(int(v))
print(ages)

min = ages[0]
for j in range(1, i):
    if ages[j] < min:
        min = ages[j]

for j in range(i):
    for k, v in friends[j].items():
        if v == str(min):
            print(
                f"Самым молодым в нашем списке друзей является {k} = {v} лет")
