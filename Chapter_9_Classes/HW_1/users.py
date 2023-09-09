# Nathan Reid
# Sept. 5th, 2022
# Make a class called User.
# Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user's information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.


# create a class
class User():
    """Create and modle a user profile information"""

    def __init__(self, first_name, last_name, age, username, location):
        """Initialize first name and last name attributes."""
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age
        self.username = username
        self.location = location

    def describe_user(self):
        """Describe the user."""
        print("This is the information in the user's profile: ")
        print(self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username.title())
        print("Age: " + str(self.age))
        print("Location: " + self.location.title())


    def greet_user(self):
        """Greet the user."""
        print("Hello, " + self.username + ". Your current location is " + self.location.title() + ". We have listed you are " + str(self.age) + ".\n")


user_1 = User('Nate', 'Reid', 37,'ncr', 'virginia')
user_2 = User('Terrance', 'Crawford', 36,'t-box', 'nebraska')
user_3 = User('Jamal', 'Small', 68, 'the_professor', 'new york')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()