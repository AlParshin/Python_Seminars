import datetime


def log_import(result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(
            f'Искались следующие люди: {str(result)}. Время запроса: {str(datetime.datetime.now())}')
        file.write('\n')


def log_export(result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(
            f'Добавлены следующие люди: {result}. Время запроса: {str(datetime.datetime.now())}')
        file.write('\n')
