

#### Конструктор экземпляра

class Person:
    max_up = 3


    def __init__(self):
        self.level = 1
        self.health = 100


p1 = Person()
p2 = Person()
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health =}')    # AttributeError: type object 'Person' has no attribute 'level'
# print(f'{Person.max_up = }, {Person.health =}')    # AttributeError: type object 'Person' has no attribute 'health'

Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')
print('------------------------')


#### Параметр self 

class Person:
    max_up = 3


    def __init__(self):
        self.level = 1
        self.health = 100
        print(f'{id(self) = }')


p1 = Person()
print(f'{id(p1) = }')
p2 = Person()
print(f'{id(p2) = }')
print('------------------------')


#### Передача аргументов в экземпляр

class Person:
    max_up = 3
    
    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')
print('------------------------')
