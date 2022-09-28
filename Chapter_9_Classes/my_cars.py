# Nathan Reid
# Sept. 8th, 2022
# Importing Multiple Classes 

from car import Car
# from car import Car, ElectricCar
# ElectricCar is in a different file

# instance 
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

import car 
# importing entire module

my_beetle = car.Car('volkswagen', 'beetle', 2018)
# variable = module.Class(arguments)
print(my_beetle.get_descriptive_name())