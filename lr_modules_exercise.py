# Create 2 new Python files. 
# In one file, write a function that will generate a number 
# between 1 and 6. Make this a module called dice.
# - write a function
# - use the random module
# - use the randint() function from random
# - return the random number

# def dice(roll):
#     import random
#     return random.randint(1, 6)
    
import lr_functions

for temploopvar in [1,1]:
    returnvar = lr_functions.dice('Roll the Dice')
    print(returnvar)


# In the second file, use the dice module to simulate throwing
#  2 dice and print the values you get from the dice.
# 