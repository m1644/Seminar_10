

''' Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
'''

class Person:
    def __init__(self, first_name, last_name, patronymic, age, phone_number, city):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self._age = age
        self.phone_number = phone_number
        self.city = city

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    @property
    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, first_name, last_name, patronymic, get_age, phone_number, city, employee_id):
        super().__init__(first_name, last_name, patronymic, get_age, phone_number, city)
        self.employee_id = employee_id

    @property
    def access_level(self):
        return self.employee_id % 7


employee1 = Employee("Иван", "Иванов", "Иванович", 30, "+7(123)456-78-90", "Москва", 123456)

print(f'ФИО: {employee1.full_name()}\n\
Возраст: {employee1.get_age}\n\
Телефон: {employee1.phone_number}\n\
Город: {employee1.city}\n\
Идентификационный номер: {employee1.employee_id}\n\
Уровень доступа: {employee1.access_level}')
