# 3. Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.
# Ввод:
# >> 3 # Количество друзей
# >> Иван
# >> 12
# >> Иннокентий
# >> 20
# >> Леша
# >> 10
# Вывод:
# >> 14
# >> Иннокентий

print("Введите количество друзей:")
i = int(input())

friends = []
names = []
ages = []

for _ in range(i):
    friends.append(
        dict([input('Введите ключ и значение через пробел:').split()]))
print(friends)

for j in range(i):
    for k, v in friends[j].items():
        ages.append(int(v))
        names.append(k)

avrg = 0

for j in range(i):
    avrg += ages[j]
avrg = avrg / i

max_length = 0

for j in range(i):
    if len(names[j]) > max_length:
        max_length = len(names[j])

print(f"Средний возраст друзей равен {avrg}")

for j in range(i):
    for k, v in friends[j].items():
        if len(k) == max_length:
            print(
                f"Самое длинное имя из друзей - {k}, состоящее из {max_length} букв")
