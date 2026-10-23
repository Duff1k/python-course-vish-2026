'''
try:
    код, в котором может возникнуть исключение
except ТипИсключения
    что делать если эта ошибка случилась
'''
file = open('numbers.txt', 'r', encoding='utf-8')
try:
    total = 0
    for row in file:
        total += int(row)
    print('Сумма: ', total)
except ValueError as error:
    print('В файле не число')
finally:
    file.close()
    print('Файл закрыт')

with open('marks.txt', 'r', encoding='utf-8') as file:
    print(file.read())

print('Файл закрыт:', file.closed)






