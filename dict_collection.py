person_list = ['Аня', 20, 'Москва']
print(person_list[2])

person = {'name': 'Аня', 'age': 20, 3: 'Москва'}
print(person[3])

person_new = dict(name='Аня', age=20, city='Москва')
print(person_new)

person_empty_dict = {}

students = ['Аня', 'Борис', 'Вика']
journal = dict.fromkeys(students, 5)
print(journal)


cities = ['Москва', 'Казань', 'Москва', 'Сочи', 'Омск', 'Казань']
print(list(dict.fromkeys(cities)))

d = {
    1: 'число',
    'имя': 'строка',
    (55.75, 37.62): 'Координаты Москвы',
    True: 10
}

print(d[(55.75, 37.62)])
#print(d['пилатес'])

prices = {'хлеб': 50, 'молоко': 90}
prices['сыр'] = 200
print(prices)

prices['хлеб'] = 60
print(prices)

prices['молоко'] += 30
print(prices)

del prices['молоко']
print(prices)

print(prices.get('хлеб'))
print(prices.get('торт'))
print(prices.get('торт', 10))

print(prices)

prices.setdefault('торт', 500)

print(prices)

#del prices['торт']


anketa = 'Иван Иванов 22 Казань Python Math Sql Git'
anketa_list = anketa.split()
print(anketa_list)

profile = {
    'name': anketa_list[0],
    'surname': anketa_list[1],
    'age': anketa_list[2],
    'city': anketa_list[3],
    'skills': anketa_list[4:],
}

print(len(profile))

print('middle_name' not in profile)

for i in profile:
    print(profile[i])

profile.clear()
print(profile)


order = {'пицца': 600, 'сок': 150, 'салаат': 300}

print(order.keys())
print(order.values())

print(list(order.keys()))

for price in prices.values():
    print('Цена: ', price)

print('Общая сумма всех цен: ', sum(prices.values()))
print('Самая высокая цена: ', max(prices.values()))



'''
price = order.pop('сок')
print('Убрали сок: ', price)
print(order)

last = order.popitem()
print(last)
print(order)
'''

print(prices.items())

for product, price in prices.items():
    print(product, 'стоит', price, 'рублей')

