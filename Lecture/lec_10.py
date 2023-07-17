

#### Полиморфизм

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
        else:
            self.level = self._max_level

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2


p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
p2 = Person('Маг', 'Тролль')

print(f'{p1.health = }, {p2.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }')
p2.change_health(p1, 10)
print(f'{p1.health = }, {p2.health = }')
print('------------------------')


path_1 = '/home/user'
path_2 = '/my_project/workdir'
# result = path_1 / path_2    # TypeError: unsupported operand type(s) for /: 'str' and 'str'
print('------------------------')


class DivStr(str):
    def __init__(self, obj):
        self.obj = str(obj)

    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj
        
        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)
        
        if first and second:
            return DivStr(start[:-1] + finish)
        
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        
        if not first and not second:
            return DivStr(start + '/' + finish)


path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2
print(f'{result = }, {type(result)}')
print(f'{result / "text" = }')
print(f'{result / 42 = }')
print(f'{result * 3 = }')
