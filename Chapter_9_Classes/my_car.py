# Nathan Reid
# Sept. 8th, 2022
# Importing Classes 

# import from a different file
from car import Car 

# Make a instance
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()