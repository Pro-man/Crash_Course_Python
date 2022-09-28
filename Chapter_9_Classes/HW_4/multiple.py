# Nathan Reid
# Sept. 8th, 2022
# Store the User class in one module, and store the Privileges and 
# Admin classes in a separate module.
# In a separate file, create an Admin instance and 
# call show_Privileges() to show that everything is still working correctly. 

from web_2 import Privileges, Admin


website = Admin('A.C.', 'Reid', 44, 'Rich_Coder', 'VA')
# website.describe_user()
website.privileges.show_privileges()