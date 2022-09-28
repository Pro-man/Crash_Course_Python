# Nathan Reid
# Sept. 2nd, 2022
# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs.
# Print the dictionary that's returned to make sure all the information was stored correctly.


# function definition with arbitrary keyword arguments
def car_summary(manufacturer,model,**car_info):
    """Store information about a car in a dictionary."""
    # create empty dictionary
    c_profile = { }
    c_profile['car_manufacturer'] = manufacturer
    c_profile['car_ model'] = model
    # loop through the dictionary
    for key, value in car_info.items():
        c_profile[key] = value
    # return the dictionary 
    return c_profile

car_information = car_summary('subaru','outback', color='grey', weather_package=True)

print(car_information)