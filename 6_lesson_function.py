'''
def имя_функции:
    тело_фнукции
'''

def print_header():
    print('=' * 25)
    print('Маганиз Ромашка')
    print('=' * 25)

print_header()
print('Хлеб - 50 рублей')

print_header()
print('Колбаса - 70 рублей')

print_header()
print('Дошик - 20 рублей')

print_header()
print('Стейк - 500 рублей')

print_header()
print('Молоко - 70 рублей')


def greet(name):
    print("Добрый день", name)

#greet('Аня', 'Борис')

students = ['Аня', 'Вадим', 'Игнат', 'Генадий']
for student in students:
    greet(student)

def print_square(number):
    print(number * number)

for i in range(1, 10):
    print_square(i)

def check_even(number):
    if number % 2 == 0:
        print(number, 'четное')
    else:
        print(number, 'нечетное')

check_even(10)
check_even(7)

def print_factorial(n):
    result = 1
    for i in (range(1, n + 1)):
        result = result * i
    print('Факториал числа', n, '=', result)


print_factorial(3)
print_factorial(5)

for number in range(1, 11):
    print_factorial(number)

def greet(name):
    print('привет!', name)


def print_square(number):
    return number * number

result = print_square(5)
print(result)

if print_square(5) > 10:
    print('Введенный квадрат больше 10')

def test():
    print('Строка до return')
    return 'результат'
    print('Строка после return')

result = test()
print(result)


def first_negative(numbers):
    for number in numbers:
        print('Проверяю', number)
        if number < 0:
            return number
    return 'отрицательных чисел нету'

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(7))

def sum_and_diff(a, b):
    return [a + b, a - b]

result = sum_and_diff(5, 2)
print(result, type(result))

'''
def ask_number(question):
    number = int(input(question))
    return number

a = ask_number("Введите первое число: ")
b = ask_number("Введите второе число: ")
print('Сумма:',a + b)
'''
'''
локальная - внутри функции
глобальная - то что вне функции
встроенная - то что Python дает сразу (print, len, abs и остальное)
'''

city = 'Москва'

def show_city():
    city = 'Санкт-Петербург'
    print('Функция видит город:', city)

show_city()
print('Снаружи тоже', city)



def add_visit(count):
    return count + 1

visits = 0
visits = add_visit(visits)
print('Посещений', visits)

print(visits)

def abs(number):
    return number * number

print(abs(-5))

def describe_pet(name, animal):
    print(name, '- это', animal)

describe_pet('Барсик', 'Кот')

describe_pet('Кот', 'Барсик')
describe_pet(animal='Кот', name='Барсик')

#describe_pet('Мурка', animal='Кошка')

def greet(name, greeting='Привет'):
    print(greeting, name)

greet('Аня')
greet('Аня', 'Здравствуйте')
greet('Аня', greeting='Добрый вечер')


students = ['Аня', 'Ваня', 'Борис', 'Николай']

def add_student(student):
    students.append(student)

add_student('Никита')

print(students)

first, *rest = [10, 20, 40, 70, 90]
print(first)
print(rest)


def show_args(*args):
    print(args)
    print(type(args))

show_args(1,2,3,5)
show_args('Кот')
show_args()



def ex_function():
    def inner_function():
        print("Это вложенная функция")
    inner_function()

