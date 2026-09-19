print(5 >= 5)
print(5 < 3)
print(5 == 5)
print(5 <= 7)
print(5 >= 7)

age = int(input())


if age >= 18:
    print("Доступ разрешен")

print("Программа продолжает работу")

shopping_list = []

if shopping_list:
    print("В списке у нас есть товары")

age = 20
has_id = False
is_vip = False

if (age >=18 and has_id) or is_vip:
    print("Билет продан")
else:
    print("Билет не продан")

day = 'суббота'
if day == 'суббота' or day == 'воскресенье':
    print('Сегодня выходной!')
else:
    print('Рабочий день')

is_raining = True

if not is_raining:
    print("Можно гулять без дождя")


print("Программа продолжает работу")



score = 80
if score >= 90:
    print("Отлично")
elif score >= 70:
    print("Хорошо")
elif score >= 50:
    print("Удовлетворительно")
else:
    print("Плохо")


age = 20
has_id = False

if age >= 18:
    print("Человек совершеннолетний")
    if has_id:
        print("Билет продан")
    else:
        print("Нет паспорта")
else:
    print("Билет не продан")



i = 20

while i >= 1:
    print(i)
    i -= 1

print("Цикл завершился")

correct_pass = '12345'
input_pass = input("Введите пароль: ")
attempts = 0
max_attempts = 4

while correct_pass != input_pass and attempts < max_attempts:
    attempts += 1
    print("Пароль неверный, попробуейте снова")
    print("Кол-во попыток: ", attempts)
    input_pass = input("Повторно введите пароль: ")

fruits = ['apple', 'banana', 'orange', 'strawberry', 'orange', 'orange', 'orange']
print(fruits)

while 'orange' in fruits:
    fruits.remove('orange')

print(fruits)


age = 15

while age < 24:
    age = age + 1
    print(age)
    if 21 >= age >= 18:
        print("Алкоголь доступен только легкий")
    elif age > 21:
        print("Любой алкоголь на выбор")
    else:
        print("Алкоголь не доступен")

numbers = [4, 7, 3, 2, 5]
target = 2
index = 0

while index < len(numbers):
    print(numbers[index])
    if numbers[index] == target:
        print("Нашли: ",numbers[index])
        break
    index += 1
else:
    print(f"{target} не найдено в списке")



