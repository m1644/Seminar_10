

''' Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
'''

class Fish:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def show_info(self):
        print(f"Вид рыбы: {self.species}")


class Bird:
    def __init__(self, name, age, wingspan):
        self.name = name
        self.age = age
        self.wingspan = wingspan

    def show_info(self):
        print(f"Размах крыльев: {self.wingspan} см")


class Mammal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def show_info(self):
        print(f"Место обитания: {self.habitat}")


fish1 = Fish("Карась", 2, "Карповые")
bird1 = Bird("Синица", 1, 15)
mammal1 = Mammal("Тигр", 5, "Лес")

print("Информация о рыбе:")
print(f'Имя: {fish1.name}, Возраст: {fish1.age}')
fish1.show_info()

print("\nИнформация о птице:")
print(f'Имя: {bird1.name}, Возраст: {bird1.age}')
bird1.show_info()

print("\nИнформация о млекопитающем:")
print(f'Имя: {mammal1.name}, Возраст: {mammal1.age}')
mammal1.show_info()
