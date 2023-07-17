

''' Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")


class Fish(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def show_info(self):
        super().show_info()
        print(f"Вид рыбы: {self.species}")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def show_info(self):
        super().show_info()
        print(f"Размах крыльев: {self.wingspan} см")


class Mammal(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def show_info(self):
        super().show_info()
        print(f"Место обитания: {self.habitat}")


fish1 = Fish("Карась", 2, "Карповые")
bird1 = Bird("Синица", 1, 15)
mammal1 = Mammal("Тигр", 5, "Лес")

print("Информация о рыбе:")
fish1.show_info()
print("\nИнформация о птице:")
bird1.show_info()
print("\nИнформация о млекопитающем:")
mammal1.show_info()
