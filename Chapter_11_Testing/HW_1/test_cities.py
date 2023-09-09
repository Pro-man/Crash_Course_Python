# Nathan Reid
# Sept. 18th, 2022
# Testing def location function 

import unittest
from city_functions import location 

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_location(self):
        """Does a simple city and country pair work?"""
        formatted_location = location('Santiago','Chile')
        self.assertEqual(formatted_location,'Santiago,Chile')

    def test_city_country_population(self):
        """Does population added to the pair work?"""
        formatted_location = location( 'Santiago','Chile','500000')
        # self.assert has to be the exact output you want for the test to work
        self.assertEqual(formatted_location, 'Santiago,Chile - population 500000')



unittest.main()