import random
import supermodule


######## Основы ООП в Python

#### Классы

data = list((1, 2, 3))
print(f'{data =  }, {type(data) = }, {type(list) = }')
print('------------------------')


result1 = random.randint(1, 10)
result2 = supermodule.randint(42)
print(f'{result1 = }')
print(f'{result2 = }')
print('------------------------')


#### Экземпляры класса

class Person:
    max_up = 3


p1 = Person()
print(f'{p1.max_up = }')


print(f'{Person.max_up = }')
print('------------------------')


#### Атрибуты класса и экземпляров

class Person:
    max_up = 3


p1 = Person()
p2 = Person()
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

p1.max_up = 12
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

Person.max_up = 44
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
print('------------------------')
