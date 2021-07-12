stuff = ["apple","orange","pear","melon"]

if "melon" in stuff:
    print("Truue")




class User:
    active_users = []

    def __init__(self, name, age):
       self.name = name
       self.age = age
       User.active_users.append(self)



user1 = User("Tyler",27)
user2 = User("Kanye", 40)
user3 = User("tom",24)


for user in User.active_users:
    print(user.name)