file = open('numbers.txt', encoding='utf-8')
total = 0
for row in file:
    total += int(row)
file.close()
print('Сумма', total)


