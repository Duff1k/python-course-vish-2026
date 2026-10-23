import sys

point = (10, 20, 30)
print(len(point))
print(15 in point)
print(15 not in point)
print(min(point))
print(max(point))
print(sum(point))
print(point, type(point))

mixed_tuple = (10, 'текстж',3.14, True, [1, 2, 4])
print(mixed_tuple, type(mixed_tuple))

empty_tuple = ()
print(empty_tuple, type(empty_tuple))

not_tuple = (5,)
print(not_tuple, type(not_tuple))

colors = 'красный', 'зеленый', 'черный'
print(colors, type(colors))

name, age, city = ('Борис', 30, 'Москва')
print(name, age, city)

t1 = tuple([1, 2, 5])
print(t1, type(t1))

print(tuple('кот'))

t = tuple()

a = (10, 20)
b = (30, 40)
print(a + b)
print(b + a)
print(a + b == b + a)

print(a * 5)

days = ('пн', 'вт', 'ср', 'чт', 'пт', 'cб', 'вскр')
print(days[0])
print(days[-1])
print(days[1:4])
print(days[3:])

for day in days:
    print(day)

for i in range(len(days)):
    print(days[i])

lst = [10, 20, 40]
lst[1] = 99
print(lst)

tpl = (10, 20, 40)
temp = list(tpl)
temp[1] = 99
tpl = tuple(temp)
print(tpl)

marks = (5, 4, 3, 5, 2, 5, 3, 3)
print(marks.count(5))
print(marks.index(3))

cities = {
    (55.75, 37.62):'Москва',
    (59.94, 30.31):'Санкт-Петербург'
}

print(cities[(55.75, 37.62)])

memory_check_lst = [1, 2, 4, 5]
memory_check_tuple = (1, 2, 4, 5)

print('Список:', sys.getsizeof(memory_check_lst), 'байт')
print('Кортеж:', sys.getsizeof(memory_check_tuple), 'байт')

students = [('Аня', 10), ('Борис', 7), ('Дмитрий', 5)]
for name, mark in students:
    print(name, 'получил оценку', mark)

numbers = [1, 2, 3, 5]
letters = ['a', 'b', 'c', 'd', 'e']
days = ('пн', 'вт', 'ср', 'чт', 'пт', 'cб', 'вскр')

result = list(zip(numbers, letters, days))
print(result, type(result))



