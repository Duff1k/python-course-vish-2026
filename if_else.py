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