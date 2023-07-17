import math


''' Задание №1
Создайте класс окружность.
* Класс должен принимать радиус окружности при создании экземпляра.
* У класса должно быть два метода, возвращающие длину окружности и её площадь.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


radius = float(input('Введите радиус окружности: '))
circle_instance = Circle(radius)

circumference = circle_instance.get_circumference()
area = circle_instance.get_area()

print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь окружности: {area:.2f}")
