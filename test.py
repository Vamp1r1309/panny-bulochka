

filename = 'test1.txt'
# fileopen = open(filename, 'r', encoding='utf-8')
# try:
#     fileopen.writelines('Моя вторая запись\n')
# except Exception as ex:
#     print('Ошибка', ex)
# finally:
#     fileopen.close()


with open(filename, 'r', encoding='utf-8') as file:
    file.read()
