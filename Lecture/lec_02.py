

#### Динамическая структура класса

class Person:
    max_up = 3


p1 = Person()
p2 = Person()
Person.level = 1
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

p1.health = 100
# print(f'{Person.health = }, {p1.health = }, {p2.health = }')    # AttributeError: type object 'Person' has no attribute 'health'
# print(f'{p1.health = }, {p2.health = }')    # AttributeError: 'Person' object has no attribute 'health'
print(f'{p1.health = }')
print('------------------------')


#### Динамическая структура класса

class Person:
    max_up = 3


p1 = Person()
p1.level = 1
p1.health = 100

dict_p1 = {}    # noqa
dict_p1['level'] = 1
dict_p1['health'] = 100

print(f'{p1.health = }')
print(f'{dict_p1["health"] = }')
print(f'{dict_p1 = }')
print('------------------------')
