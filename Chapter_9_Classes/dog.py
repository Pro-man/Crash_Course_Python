# Nathan Reid
# Sept. 4th, 2022
# Classes

# NOTE - Instantiation -> Making an object from a class and you work with instances of a class.

# Capitalize names refer to classes / empty () because we are creating this class from scratch
class Dog():
    """A simple attempt to model a dog."""
    # special method that Python runs automatically whenever we create a new instance based on the Dog class.
    # Thhe self parameter is always first 
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # any variable prefixed with self is available to every method in the class
        # Variables that are accessible through instances like this are called attributes
        self.name = name
        self.age = age 

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in reponse to a command."""
        print(self.name.title() + " rolled over!")

# NOTE - Think of a class as a set of instructions for how to make an instance. 

# Return the class in a variable / with positional arguments
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

# Call the methods in the class
# To call a method, give the name of the instance and method you want to call, separated by a dot
my_dog.sit()
my_dog.roll_over()

# To access the atributes of an instance, use dot notation then the parameter
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# NOTE - You can make as many instances from one class as you need, as long as you give each
# instance a unique variable name or it occupies a unique spot in a list or dictionary.

