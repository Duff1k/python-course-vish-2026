from tkinter.font import names


def greet(name):
    print('Привет', name)

first, last, *second = [10, 20, 30, 40, 50]
print(first)
print(last)
print(second)


def show_args(*args):
    print(args)
    print(type(args))

show_args(1, 2, 3)
show_args('кот')
show_args()

def total(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(total(1,2,3))
print(total(5,20,30,440, 50))
print(total())

def greet_all(greeting, *names):
    for name in names:
        print(greeting, name)

#greet_all('Привет', 'Аня', 'Вова', 'Паша')
#greet_all('Aloha', 'Павел')
#greet_all(greeting='Дарова', 'Аня', 'Ваня', 'Никита')


def average_marks(name, *marks):
    if len(marks) == 0:
        print(name, 'оценок пока нет')
    else:
        print(name, 'средний балл:', round(sum(marks) / len(marks)))

average_marks('Иван', 5, 3, 2, 4, 5)
average_marks('Борис', 3, 4)
average_marks('Вика')

def show_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

show_kwargs(name='Аня', age=30)
show_kwargs(average_marks=4)
show_kwargs()

def print_profile(**info):
    print('------Анкета-----')
    for key, value in info.items():
        print(key, value)

print_profile(name='Иван', age=20, city='Moscow')
print_profile(fio='Иванов Иван Иваныч', hobbies=['Шахматы', 'Волебол'])\

def show_settings(**settings):
    theme = settings.get('theme', 'светлая')
    language = settings.get('language', 'русский')
    print(f'Тема: {theme}, Язык: {language}')

show_settings()
show_settings(theme='темная')
show_settings(language='английский')

def make_pizza(size, *toppings, **details):
    print('Пицца размера', size)
    print('Добавки:', toppings)
    for topping in toppings:
        print('-',topping)
    print('Детали заказа', details)
    for key, value in details.items():
        print(key, value)

make_pizza('Большая', 'сыр', 'грибы', 'оливки',
           address='НИЯУ МИФИ', time='19:00')

make_pizza('Маленькая')
