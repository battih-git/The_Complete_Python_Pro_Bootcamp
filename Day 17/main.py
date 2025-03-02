class User:
    # Defining init method to pass attributes whenever we construct new object
    def __init__(self,user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0 # Default value for the attribute. It's not necessary to pass it, when creating an object
        self.following = 0
        print("new user being created.")

    # Creating a function to follow.
    def follow(self, user):
        user.followers += 1
        self.following += 1



# Creating user with class User
user_1 = User(2,"huzefa")
user_2 = User(3,'angela')
user_1.follow(user_2)
user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_1.following)