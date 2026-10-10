from queue import PriorityQueue

from base import fruits

a = {5, 'привет', True, 'привет', 5, 5, 5, 'Пока'}
print(a, type(a))

b = set('программа')
print(b)
print(len(b))

c = {'программа'}
print(c)
print(len(c))

numbers = [5, 3, 5, 1, 3, 3, 7]
unique_numbers = set(numbers)
print(numbers)
print(unique_numbers)

set_from_range = set(range(10))
print(set_from_range)

first_empty_set = set()
print(first_empty_set, type(first_empty_set))

second_empty_set = {}
print(second_empty_set, type(second_empty_set))

'''
third_set = set([[1,2], [3,4]])
print(third_set)
'''

cities = ['Москва', 'Казань', 'Москва', 'Сочи', 'Омск', 'Казань']
print('Было:', cities, type(cities))

unique_cities = list(set(cities))
print('Стало: ',unique_cities, type(unique_cities))

s = {1, 2, 3}
s.add(4)
print(s)

s.add(2)
print(s)

s.update([5, 6, 7])
print(s)

s.update({6, 10, 12})
print(s)

s.update([17,20,30], {17, 50, 20})
print(s)

colors = {'красный', 'синий', 'зеленый'}
colors.discard('синий')
print(colors)

colors.discard('черный')
print(colors)

colors.remove('зеленый')
print(colors)

fruits = {'яблоко', 'банан', 'груша'}
taken = fruits.pop()
print('Достали: ', taken)
print('Осталось: ', fruits)

tasks = {'Задача 1', 'Задача 2', 'Задача 3'}

while tasks:
    task = tasks.pop()
    print('Выполняю задачу: ', task)

print('Осталось задач: ', tasks)

numbers = {1, 2, 3, 7, 10}
numbers.clear()
print(numbers)

python_students = {'Аня', 'Никита', 'Андрей', 'Иван', 'София'}
java_students = {'Андрей', 'Борис', 'Дима', 'Ева'}
print(python_students & java_students)
print(python_students.intersection(java_students))

print(python_students | java_students)
print(python_students.union(java_students))

print(python_students - java_students)
print(java_students - python_students)

print(python_students ^ java_students)
print((python_students - java_students) | (java_students - python_students))

print({1, 2, 3} == {3,2,1})
print([1,2,3]==[3,2,1])
print({1,2,2,2,2,3} == {1,2,3})

print({1,2} < {1,2,3})
print({1,4} < {1,2,3})
print({1,2,3} <= {1,2,3})
print({1,2}.issubset({1,2,3}))

'''
animals = {'кот', 'собака', 'хомяк'}
for i in range(len(animals)):
    print(animals[i])

range(3) -> 0, 1, 2

'''

text = 'мама мыла раму'
print(text.split())

date = '09.10.2026'
print(date.split('.'))

unique_words = set()
line = input('Введите строку: ')
while line != '':
    words = line.lower().split()
    unique_words.update(words)
    line = input('Введите строку: ')

print('Уникальные слова: ', unique_words)






