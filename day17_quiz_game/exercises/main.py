ID_NUMBER_LENGTH = 3


class User:
    number_of_users = 0

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

        User.number_of_users += 1
        print(f"User number {User.number_of_users} was created !")
        print(f"User ID is {self.user_id}")

    def follow(self, user):
        user.followers += 1
        self.following += 1


class Database:
    ...


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Matthew"

for i in range(1, 10000):
    id_num = str(i).rjust(ID_NUMBER_LENGTH, "0")
    user = User(id_num, "Noname")
    # print(f"User name is {user.username}")
    if i % 5 == 0:
        pass
