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