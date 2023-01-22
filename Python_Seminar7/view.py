def inp_mod():
    mod = input('Введите режим работы: "импорт" или "экспорт": ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def view_import(result):
    print(*result, sep='\n')


def view_import_no():
    print('Людей с такой фамилией не найдено')


def inp_export():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    sec_name = input('Введите отчество: ')
    phone = input('Введите телефоон: ')
    comment = input('Введите тип телефона: ')
    return '\n', surname, name, sec_name, phone, comment