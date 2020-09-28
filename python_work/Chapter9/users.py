#  Users: Make a class called User. Create two attributes called first_name and last_name,
#  and then create several other attributes that are typically stored in a user profile.
#  Make a method called describe_user() that prints a summary of the user’s information.
#  Make another method called greet_user() that prints a personalized greeting to the user.
#  Create several instances representing different users, and call both methods for each user.

class User:
    """Creating a user"""
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.username = username

    def describe_user(self):
        """Describing a user"""
        print(f' First Name: {self.first_name.title()}')
        print(f' Last Name: {self.last_name.title()}')
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        print(f'\n Hello {self.username}!')


user1 = User('carolina', 'rolo', 'c_rolo', 'carol.rolo@hotmail.com', 'floripa')
user1.describe_user()
user1.greet_user()

user2 = User('carla', 'rolo', 'carlinha', 'carlota.rolo@hotmail.com', 'sao paulo')
user2.describe_user()
user2.greet_user()
