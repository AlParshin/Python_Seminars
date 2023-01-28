# Задача про кофе:

# На заводе «Кофейный» открывается новое кафе. Изначально есть некоторое количество кофейных зерен, молока и взбитых сливок.
# Надо написать функцию choose_coffee(preference1, preference2, ..., preferenceN), которая
# возвращает напиток, который можно приготовить из имеющихся продуктов(ingredients).
# На вход функция принимает заранее неизвестное количество предпочтений посетителя.
# Все напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
# Бариста готовит наиболее предпочитаемый напиток из доступных.

# Для Эспрессо требуется: 1 порция кофейных зерен.
# Для Капучино требуется: 1 порция кофейных зерен и 3 порции молока.
# Для Маккиато требуется: 2 порции кофейных зерен и 1 порция молока.
# Для Кофе по-венски требуется: 1 порция кофейных зерен и 2 порции взбитых сливок.
# Для Латте Маккиато требуется: 1 порция кофейных зерен, 2 порции молока и 1 порция взбитых сливок.
# Для Кон Панна требуется: 1 порция кофейных зерен и 1 порция взбитых сливок.

# При приготовлении напитка ингредиенты расходуются.
# Если недостаточно ингредиентов, то вернуть сообщение: «К сожалению, не можем предложить Вам напиток».

def kofe():
    zerna = int(input("Введите количество порций кофейных зерен в наличии: "))
    moloko = int(input("Введите количество порций молока в наличии: "))
    slivki = int(input("Введите количество порций сливок в наличии: "))
    print({'Зерна': zerna, 'Молоко': moloko, "Сливки": slivki})
    nalichie = [zerna, moloko, slivki]
    espresso = [1, 0, 0]
    kapuchino = [1, 3, 0]
    makkiato = [2, 1, 0]
    venskiy = [1, 0, 2]
    latte = [1, 2, 1]
    konpanna = [1, 0, 1]
    print("Напишите Ваш заказ:")
    count_espresso = int(input("Сколько порций ЭСПРЕССО (1,0,0) заказываем: "))
    count_kapuchino = int(
        input("Сколько порций КАПУЧИНО (1,3,0) заказываем: "))
    count_makkiato = int(input("Сколько порций МАККИАТО (2,1,0) заказываем: "))
    count_venskiy = int(input("Сколько порций ПО-ВЕНСКИ (1,0,2) заказываем: "))
    count_latte = int(
        input("Сколько порций ЛАТТЕ МАККИАТО (1,2,1) заказываем: "))
    count_konpanna = int(
        input("Сколько порций КОН ПАННА (1,0,1) заказываем: "))
    for i in range(3):
        if (nalichie[i] - (count_espresso*espresso[i] + count_kapuchino*kapuchino[i] + count_makkiato*makkiato[i] + count_venskiy*venskiy[i] + count_latte*latte[i] + count_konpanna*konpanna[i])) < 0:
            print('Весь Ваш заказ целиком мы приготовить не сможем, не хватает ингридиентов. Посмотрим, что из заказа можно сделать...')
            break
    final_list = []
    # Приоритет напитков выбран по принципу "от большего количества требуемых ингридиентов до меньшего: от капучино и латте (по 4 порции в каждом) до эспрессо (1 порция)"
    if count_kapuchino > 0:
        for _ in range(count_kapuchino):
            if ((nalichie[0] - kapuchino[0]) >= 0) and ((nalichie[1] - kapuchino[1]) >= 0) and ((nalichie[2] - kapuchino[2]) >= 0):
                nalichie[0] = nalichie[0] - kapuchino[0]
                nalichie[1] = nalichie[1] - kapuchino[1]
                nalichie[2] = nalichie[2] - kapuchino[2]
                final_list.append('капучино')
    if count_latte > 0:
        for _ in range(count_latte):
            if ((nalichie[0] - latte[0]) >= 0) and ((nalichie[1] - latte[1]) >= 0) and ((nalichie[2] - latte[2]) >= 0):
                nalichie[0] = nalichie[0] - latte[0]
                nalichie[1] = nalichie[1] - latte[1]
                nalichie[2] = nalichie[2] - latte[2]
                final_list.append('латте')
    if count_venskiy > 0:
        for _ in range(count_venskiy):
            if ((nalichie[0] - venskiy[0]) >= 0) and ((nalichie[1] - venskiy[1]) >= 0) and ((nalichie[2] - venskiy[2]) >= 0):
                nalichie[0] = nalichie[0] - venskiy[0]
                nalichie[1] = nalichie[1] - venskiy[1]
                nalichie[2] = nalichie[2] - venskiy[2]
                final_list.append('по-венски')
    if count_makkiato > 0:
        for _ in range(count_makkiato):
            if ((nalichie[0] - makkiato[0]) >= 0) and ((nalichie[1] - makkiato[1]) >= 0) and ((nalichie[2] - makkiato[2]) >= 0):
                nalichie[0] = nalichie[0] - makkiato[0]
                nalichie[1] = nalichie[1] - makkiato[1]
                nalichie[2] = nalichie[2] - makkiato[2]
                final_list.append('маккиато')
    if count_konpanna > 0:
        for _ in range(count_konpanna):
            if ((nalichie[0] - konpanna[0]) >= 0) and ((nalichie[1] - konpanna[1]) >= 0) and ((nalichie[2] - latte[2]) >= 0):
                nalichie[0] = nalichie[0] - konpanna[0]
                nalichie[1] = nalichie[1] - konpanna[1]
                nalichie[2] = nalichie[2] - konpanna[2]
                final_list.append('кон панна')
    if count_espresso > 0:
        for _ in range(count_espresso):
            if ((nalichie[0] - espresso[0]) >= 0) and ((nalichie[1] - espresso[1]) >= 0) and ((nalichie[2] - espresso[2]) >= 0):
                nalichie[0] = nalichie[0] - espresso[0]
                nalichie[1] = nalichie[1] - espresso[1]
                nalichie[2] = nalichie[2] - espresso[2]
                final_list.append('эспрессо')

    print('Можем приготовить Вам только следующие напитки из заказа:', final_list)
    print('По наличию остались неиспользованными ингридиенты: ', nalichie)


kofe()
