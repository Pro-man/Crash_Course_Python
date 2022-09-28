# Nathan Reid
# Sept. 7th, 2022
# Write a class called Admin that inherits from the User class you 
# wrote. Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's
# set of privileges. Create an instances of Admin, and call your method.

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
        self.login_attempts = 5

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

    def increment_login_attempts(self, attempts):
        """Increments the value of login _attempts by 1."""
        self.login_attempts += 1

    
    def reset_login_attempts(self, attempts):
        """Resets the value of login_attempts to 0."""
        self.login_attempts *= 0

# create child class
class Admin(User):
    """Create an admin profile information"""
    
    def __init__(self, first_name, last_name, age, username, location):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, age, username, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        print("\nList of Admin Privileges: ")
        for post in self.privileges:
            print("- " + post.upper())

website = Admin('A.C.', 'Reid', 44, 'Rich_Coder', 'VA')
website.describe_user()
website.show_privileges()