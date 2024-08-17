users_list = []

class User():
    def __init__(self, ID, name, access_level):
        self.ID = ID
        self.name = name
        self.access_level = access_level

class Admin(User):
    def __init__(self, ID, name, access_level):
        super().__init__(ID, name, access_level)

    def add_user(self, user):
        if self.access_level == 'admin':
            users_list.append(user.name)
            print(f'{user.name} has been added')

    def delete_user(self, user):
        if self.access_level == 'admin' and user.name in users_list:
            users_list.remove(user.name)
            print(f'{user.name} has been deleted')
        else:
            print('You are not an admin or user not found in the list')

    def show_all_users(self):
        if self.access_level == 'admin':
            print(users_list)


admin = Admin(1, 'Alex', 'admin')
user1 = User(2, 'Pamela', 'user')
user2 = User(3, 'Natalie', 'user')
user3 = User(4, 'Scarlett', 'user')

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

admin.show_all_users()

admin.delete_user(user2)
admin.show_all_users()