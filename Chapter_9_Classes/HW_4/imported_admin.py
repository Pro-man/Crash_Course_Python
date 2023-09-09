# Nathan Reid
# Sept. 8th, 2022
# Use 9-8
# Store the classes User, Privileges, and Admin in one module. 
# Create a separate file, make an Admin instance, and 
# call show_privileges() to show that everything is working correctly.

# import classes
from access import Admin, User, Privileges 

# create instance
task = Admin('Lavon', 'Johnson', 36, 'MMA_Coder', 'MD')
task.privileges.show_privileges()