###my_name = input("Как вас зовут?")
###print(f"Меня зовут {my_name}")
from pkgutil import walk_packages

age = 25
print(age)
print(type(age))

fruits = ['apple', 'orange', 10]
print(fruits)
print(type(fruits))

person = {"name": "Daniel", "age": 25}
print(person)
print(type(person))

is_authorized = True
print(is_authorized)
print(type(is_authorized))


first_name = 'Ivan'
print(first_name)
print(type(first_name))
print(dir(first_name))
print(first_name.upper())
print(first_name.lower())
print(len(first_name))

print(first_name, fruits, is_authorized)
print(first_name, fruits, is_authorized, sep='-')

print(end='Привет!')
print("Как дела ?")


print(f"Меня зовут {first_name}")
print(f"Через 5 лет мне будет: {age + 5}")

print(f"Меня зовут {first_name}, через 5 лет мне будет {age + 5}")


x = 5
print(type(x))

x = '5'
print(type(x))


a = 5
print(id(a))

a = 5 + 2
print(id(a))


b = [1,2,3]
print(id(b))

b.append(4)
print(id(b))


discription = """Первая строка
Вторая строка
Третья строка"""

print(discription)

word = 'Питоттотот'
print(len(word))
print(word[0])
print(word[3])
print(word[1:4])
print(word[4])
print(word[-1])

print(word.replace("тон", " число"))
print(word.count('т'))
print(word.index("и"))



print(pow(2, 10))

total_sum = 1_000_000
print(total_sum)
print(type(total_sum))


pi = 3.14
pi = round(pi)

g = 9.8
print(round(g))

print(bool(0)) #FALSE
print(bool(5)) #TRUE
print(bool("")) #FALSE
print(bool("Иван")) #TRUE
print(bool([])) #FALSE
print(bool([1, 2])) #TRUE
print(bool(round(0.12)))


bag_things = [10, True, 24.4, 'Yellow']
print(bag_things[0])
print(bag_things[-1])
print(len(bag_things))

bag_things[1] = False
print(bag_things)

del bag_things[-1]
print(bag_things)

matrix = [[1,2], [3,4], [5,6]]
print(matrix[0])
print(matrix[0][1])

del matrix[-1][-1]
print(matrix)




second_bag_things = [10, True, 24.4, 'Yellow']
third_bag_things = second_bag_things
third_bag_things.clear()
print(second_bag_things)

a = 10
b = a
print(id(a))
print(id(b))

c = 1000
d = 1001
print(id(c))
print(id(d))

##second_bag_things.insert(1, False)
##second_bag_things.remove(True)
##last_element = second_bag_things.pop(2)
##print(last_element)
#























