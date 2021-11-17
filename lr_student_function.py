# Create a new python file. In that file create a program that works 
# out a grade based on marks with the use of functions.

# The program should take the 
# - students name, 
# - homework score (/25), 
# - assessment score (/50) and 
# - final exam score (/100) as inputs,
# 
#  and output their name and final ICT grade as a percentage.

# Reminder: any inputs and prints should not be included inside the 
# function definition, and should strictly be done outside.

# Stretch goal: Include grade boundaries such that the program also
#  outputs a grade for the student (A, B, etc.)

def gradescore(inputscore1,inputscore2,inputscore3):
    totalscorepercent = (inputscore1 + inputscore2 + inputscore3) / 175 * 100
    return totalscorepercent


stu = input("NAME: ")
hws = int(input("HOMEWORK: "))
ass = int(input("ASSESMENT: "))
fin = int(input("FINAL EXAM: "))

returnpercentscore = gradescore(hws, ass, fin)
print(stu,returnpercentscore)