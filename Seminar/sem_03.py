

''' Задание №3
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
'''

class Person:
    def __init__(self, full_name, age, phone_number, city):
        self._full_name = full_name
        self._age = age
        self._phone_number = phone_number
        self._city = city

    def birthday(self):
        self._age += 1

    def full_name(self):
        return self._full_name

    def get_age(self):
        return self._age

    def phone_number(self):
        return self._phone_number

    def city(self):
        return self._city


person = Person("Иванов Иван Иванович", 30, "+7(123)456-78-90", "Москва")

print(f'ФИО: {person.full_name()}\nВозраст: {person.get_age()}\nТелефон: {person.phone_number()}\nГород: {person.city()}')
print('----------------Прошел год...')

person.birthday()

print(f'ФИО: {person.full_name()}\nВозраст: {person.get_age()}\nТелефон: {person.phone_number()}\nГород: {person.city()}')
