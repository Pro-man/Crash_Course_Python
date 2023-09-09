# Nathan Reid
# Aug. 27, 2022
# while loop

# while loops run as long as, a certain condition is true

# set a variable
current_number = 1
# while loop
while current_number <= 5:
    print(current_number)
    current_number += 1

# set a variable
current_num = 0
# while loop
while current_num < 10:
    # add 1 to the num once it runs
    current_num += 1
    # conditional test to see if the number is divisible by 2
    if current_num % 2 == 0:
        continue

    print(current_num)

# NOTE - To avoid wrting infinite loops, test every while loop and make sure
# the loop stops when you expect it to.

