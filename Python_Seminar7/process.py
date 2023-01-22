def search(surname):
    with open('data.txt', 'r', encoding='utf-8') as file:
        res_list = []
        while True:
            my_book = file.readline()
            if not my_book:
                if not file.readline():
                    break
            if my_book.rstrip() == surname:
                res_list.append(surname)
                for i in range(4):
                    res_list.append(file.readline().rstrip())
                res_list.append('')
    if len(res_list) > 0:
        return res_list
    return "Людей с такой фамилией не найдено"


def export(res):
    with open('data.txt', 'a', encoding='utf-8') as file:
        for ind in range(5):
            file.write(res[ind] + '\n')
        file.write(res[5])
