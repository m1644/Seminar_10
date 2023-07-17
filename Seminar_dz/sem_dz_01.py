

''' Задание_1
Доработаем задачи 5-6. 
Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
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


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age, **kwargs):
        if animal_type == "Fish":
            return Fish(name, age, kwargs.get("species", ""))
        elif animal_type == "Bird":
            return Bird(name, age, kwargs.get("wingspan", 0))
        elif animal_type == "Mammal":
            return Mammal(name, age, kwargs.get("habitat", ""))
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


fish1 = AnimalFactory.create_animal("Fish", "Карась", 2, species="Карповые")
bird1 = AnimalFactory.create_animal("Bird", "Синица", 1, wingspan=15)
mammal1 = AnimalFactory.create_animal("Mammal", "Тигр", 5, habitat="Лес")

print("Информация о рыбе:")
fish1.show_info()
print("\nИнформация о птице:")
bird1.show_info()
print("\nИнформация о млекопитающем:")
mammal1.show_info()
