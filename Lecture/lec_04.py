

#### Методы класса

class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.level = }, {p2.level = }, {p3.level = }')

p3.level_up()
p1.level_up()
p3.level_up()
print(f'{p1.level = }, {p2.level = }, {p3.level = }')
print('------------------------')


class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = }, {p3.health = }')

p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
print('------------------------')


#### Задание_1

class User:
    count = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


u1 = User('One', '123-45-67')
u2 = User('NoOne', '76-54-321')
u1.count.append(42)
u1.count.append(73)
u2.counter = 256
u2.count.append(u2.counter)
u2.count.append(u1.count[-1])
print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
print('------------------------')
