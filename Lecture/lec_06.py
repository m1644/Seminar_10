

#### Доступ к приватным переменным

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


p1 = Person('Сильвана', 'Эльф', 120)
print(f'{p1.up = }')

p1.up = 1
print(f'{p1.up = }')

for _ in range(5):
    p1.add_up()
    print(f'{p1.up = }')

print(p1._Person__max_up)
print(Person._Person__max_up)
print('------------------------')


#### Задание_2

class User:

    def __init__(self, name, phone, password):
        self.__name__ = name
        self._phone = phone
        self.__password = password


u1 = User('One', '123-45-67', 'qwerty')
print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password = }')
