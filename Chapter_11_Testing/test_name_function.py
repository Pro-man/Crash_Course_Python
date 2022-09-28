#  Nathan Reid
# Sept. 17th, 2022
# Testing Functions

# Unit test - verifies that one specific aspect of a function's behavior is correct.

# Test case - a collection of unit tests that together prove that a function behaves 
# as it's supposed to, within the full range of situations you expect it to handle.

# Full coverage - full range of unit tests covering all the possible ways you can use a function.

import unittest 
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')



unittest.main()

# Test a function
# 1 - Write a test case for the function
# 2 - import unittest module and function you want to test
# 3 - Create a class that inherits from unittest.TestCase
# 4 - Write a series of methods to test different aspects of the function

# NOTE - The best to call something related to the function you are about to test and 
# to use the word 'Test' in the class name.

# NOTE - Any method that starts with 'test_' will be run automatically when we 
# run test_name_function.py Within this test method, we call the function we want
# to test and store a return value that we're interested in testing. 

# NOTE - self.assertEqual() - compare the value in formatted_name to the string 'Janis Joplin'.

# NOTE - The line unittest.main() tells Python to run the tests in this file.

# NOTE - Assert methods verify that a result you received matches the result you expected to receive.

# NOTE - The dot on the first line of the output tells that a single test passed.
# The final OK tells that all unit tests in the test cast passed.

# For errors 
# You will see a single 'E' which tells one unit test in the test case resulted in a error.

# NOTE - The method name must start with 'test_' so the method runs automatically when we run
# test_name_function.py

# NOTE - It's fine to have a long method names in your TestCase classes.