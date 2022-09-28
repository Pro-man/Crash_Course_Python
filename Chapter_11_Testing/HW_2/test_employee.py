# Nathan Reid
# Sept. 19th, 2022
# Write a test case for Employee. 
# Write two test methods, test_give_default_raise() and test_give_custom_raise().
# Use the setUp() method so you don't have to create a new employee instance in each test method. 
# Run your test case, and make sure both tests pass.

import unittest 
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.lavon = Employee('lavon', 'matthes', 65000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.lavon.give_raise()
        self.assertEqual(self.lavon.salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.lavon.give_raise(10000)
        self.assertEqual(self.lavon.salary, 75000)

unittest.main()

# needed help with this. 