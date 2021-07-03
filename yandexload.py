import yadisk


def load_file():
    y = yadisk.YaDisk(token=input('вставьте свой токен:'))
    yadate = input('Название папки на яндекс диске:')
    y.mkdir(f'/{yadate}')
    disk = input('Какой диск:')
    date = input('Какая папка:')
    file = input('Файл с расширением:')
    y.upload(f'{disk}://{date}/{file}', f'/{yadate}/{file}')



load_file()