from tabnanny import check

numbers = [5, 2, 9, 1, 7]
#result = numbers.sort()
#numbers = sorted(numbers, reverse=True)
numbers.sort(reverse=True)
print(numbers)


print('---------------')

values = (5, 2, 9, 1, 7)
word = 'питон'

print(values)
print(word)


#sort - метод списка, sorted - встроенная функция

print(hasattr(numbers, 'sort'))
print(hasattr(values, 'sort'))
print(hasattr(word, 'sort'))

print(sorted(numbers)) #был список
print(sorted(values, reverse=True))  #был кортеж
print(sorted(word, reverse=True))    #была строка
#print(sorted([3, 'кот', True]))

animal = ['гиппопотам', 'кот', 'собака', 'еж']
print(sorted(animal, key=len))

temperatures = [-10, 8, 2, -4, 5]
print(sorted(temperatures, key=abs))

def last_two_digit(x):
    return x%10, x//10%10

digits = [45, 12, 21, 5, 11, 40]
print(sorted(digits, key=lambda x: (x%10, x//10%10)))




fruits = ['банан', 'Яблоко', 'Груша', 'апельсин']
print(sorted(fruits, key=str.lower))

def square(x):
    return x*x

square_lambda = lambda x: x*x
print(square_lambda(5))

# Нельзя f = lambda numbers: y = x + 1
# Нельзя f = lambda numbers: for number in numbers: print(number)
# Нельзя f = lambda x: if x>0: 'положительное'

#Тернальный оператор: значение_если_да if условие else значение если нет

#Пример status = 'взрослый' if age >= 18 else 'молодой'

check_age = lambda age: 'взрослый' if age >= 18 else 'молодой'
print(check_age(20))
print(check_age(12))


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

print(operations['+'](10, 5))
print(operations['-'](10, 5))
print(operations['*'](10, 5))
print(operations['/'](10, 5))


#y = kx + b
def make_linear(k, b):
    return lambda x: k*x + b

line1 = make_linear(4, 5)
print(line1(10))



print(make_linear(4, 5)(10))

result = [('Аня', 87), ('Борис', 95), ('Вика', 72), ('Глеб', 90)]
print(sorted(result, key=lambda item: item[1], reverse=True))

prices = {'хлеб': 50, 'сыр': 450, 'молоко': 90, 'кофе': 300}
print(sorted(prices))

by_price = dict(sorted(prices.items(), key=lambda item: item[1], reverse=False))
print(by_price)

students = [('Аня', 87), ('Борис', 95), ('Вика', 72), ('Глеб', 90), ('Михаил', 87)]
print(sorted(students, key=lambda s: (-s[1], s[0])))

print((1, 'б') < (2, 'a'))
print((1, 'a') > (1, 'б'))

print(max(students, key=lambda s: s[1]))
print(min(students, key=lambda s: s[1]))


top3 = sorted(students, key=lambda s: (-s[1], s[0]))[-1]
print(top3)





