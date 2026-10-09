'''
for 'ПЕРЕМЕННАЯ' in 'ИТЕРИРУЕМЫЙ_ОБЪЕКТ':
    'ТЕЛО_ЦИКЛА (ДЕЙСТВИЕ)'
'''


for i in range(5):
    print(i)

for i in range(10):
    print("ДО ИЗМЕНЕНИЯ ", i)
    i = 100
    print("ПОСЛЕ ИЗМЕНЕНИЯ", i)
    print("----------")

num = int(input("Введите число: "))
total_sum = 0
factorial = 1

for i in range(1, num+1):
    total_sum += i
    factorial *= i

print(total_sum)
print(factorial)



fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)

fio = 'Иванов Иван Иванович'
for f in fio:
    print(f)

from enum import unique

numbers = [1, 2, 3, 5, 7, 9, 12, 15]

for num in numbers:
    num = num * 2

for i in range(len(numbers)):
    numbers[i] *= 2

print(numbers)

random_numbers = [1, 2, 3, 5, 3, 3, 3, 2, 7, 9]
unique = []

for num in random_numbers:
    if num not in unique:
        unique.append(num)

print("Исходный список: ", random_numbers)
print("Уникальные: ", unique)

for i in range(1, 10):
    for j in range(1, 10):
        print(i, j, i*j)
        print()

for s in 'appleinplate':
    if s == 'n':
        break
    print(s)

word = input('Введите слово:  ')
for i in word:
    if i == 'я':
        print("Обнаружена запрещенная буква я")
    print(i)
else:
    print('Успешное завершение, запрещенных букв не обнуржено')

print('Проверка завершена')