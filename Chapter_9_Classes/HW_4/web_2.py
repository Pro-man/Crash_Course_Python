from web_1 import User

# create class
class Privileges():
    """Display the privileges of the admin."""

    def __init__(self, privileges = [ ]):
        """Initialize first name and last name attributes."""
        self.privileges = ["can add post", "can delete post", "can ban user"] 

    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        print("\nList of Admin Privileges: ")
        for post in self.privileges:
            print("- " + post.upper())


# create child class
class Admin(User):
    """Create an admin profile information"""
    
    def __init__(self, first_name, last_name, age, username, location):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, age, username, location)
        self.privileges = Privileges()
