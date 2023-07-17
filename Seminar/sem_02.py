

''' Задание №2
Создайте класс прямоугольник.
* Класс должен принимать длину и ширину при создании экземпляра.
* У класса должно быть два метода, возвращающие периметр и площадь.
* Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
'''

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None or width == "" else width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width


length = float(input("Введите длину прямоугольника: "))
width = input("Введите ширину прямоугольника (если оставить пустым, будет считаться квадрат): ")
if width:
    width = float(width)

rectangle_instance = Rectangle(length, width)

perimeter = rectangle_instance.get_perimeter()
area = rectangle_instance.get_area()

print(f"Периметр прямоугольника: {perimeter}")
print(f"Площадь прямоугольника: {area}")
