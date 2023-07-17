import json


''' Задание_2
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. 
Превратите функции в методы класса, а параметры в свойства. 
Задачи должны решаться через вызов методов экземпляра.
'''

''' Задача из прошлого семинара:
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

class UserManagement:
    def __init__(self, users_file):
        self.users_file = users_file
        self.users = {}
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            pass

    def add_user(self):
        while True:
            name = input("Введите имя пользователя (или 'exit' для завершения): ")
            if name.lower() == 'exit':
                break
            
            identifier = input("Введите личный идентификатор пользователя: ")
            access_level = int(input("Введите уровень доступа (от 1 до 7): "))
            
            if access_level not in range(1, 8):
                print("Некорректный уровень доступа. Попробуйте снова.")
                continue
            
            if identifier in self.users:
                print("Идентификатор уже занят. Попробуйте снова.")
                continue
            
            self.users[identifier] = {'name': name.encode('utf-8').decode('utf-8'), 'access_level': access_level}
            
            with open(self.users_file, 'w', encoding='utf-8') as file:
                json.dump(self.users, file, indent=4, ensure_ascii=False)
        print("Данные сохранены в файле 'users.json'.")

users_file = 'Seminar_dz/users.json'
user_management = UserManagement(users_file)
user_management.add_user()
