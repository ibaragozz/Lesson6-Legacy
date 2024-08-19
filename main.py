class User:
    def __init__(self, ID, name, access_level='user'):
        self._ID = ID
        self._name = name
        self._access_level = access_level

    # Методы для получения и изменения ID
    def get_ID(self):
        return self._ID

    def set_ID(self, ID):
        self._ID = ID

    # Методы для получения и изменения имени
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name, access_level='admin')
        self._users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users_list.append(user)
            print(f'{user.get_name()} добавлен в список')

    def remove_user(self, user):
        if user in self._users_list:
            self._users_list.remove(user)
            print(f'{user.get_name()} удален из списка')
        else:
            print(f'{user.get_name()} не найден в списке')

    def show_all_users(self):
        print("Users list:")
        for user in self._users_list:
            print(f'ID: {user.get_ID()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}')


# Пример использования:
admin = Admin(1, 'Alex')
user1 = User(2, 'Pamela')
user2 = User(3, 'Natalie')
user3 = User(4, 'Scarlett')

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

admin.show_all_users()

admin.remove_user(user2)
admin.show_all_users()
