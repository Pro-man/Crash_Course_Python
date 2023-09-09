# Nathan Reid
# Sept. 13th, 2022 
# Wrap your code from addition.py in a while loop so the user
# can continue entering numbers even if they make a mistake and 
# enter text instead of a number.

print("Give us two numbers.")
print("Enter 'q' to quit.\n")

active = True

while active:
    f_num = input("What is your first number: ")
    if f_num == 'q':
        # active = False - this allows the program to continue and end once the second iinput is done
        break
    s_num = input("What is your second number: ")
    try:
        add = int(f_num) + int(s_num)
    except ValueError:
        pass
    else:
        print(add)
