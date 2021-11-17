# For Loop

# cool_cows = ("Winnie the Moo", "Moolan", "Milkshake", "Mooana")
#cool_cows = "Winnie the Moo"
# cool_sheep = ["Baaaart", "Baaaarnaby"]
# cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

# cool_animals = [cool_cows, cool_sheep, cool_pigs]
# for loopvar in cool_animals:
#     for subloopvar in loopvar:
#         print(subloopvar)

# Looping over a Dict

# booksDict = { "Title":"Concrete for Fun","Published":1972, "Author":"Ted McPavingstone", "Cover":"Ultra-Hardback","Price":5.99 }

# for i in booksDict.keys():
#     print(booksDict[i])

# for loopvar in range(5,56,5):
#     print(loopvar, cool_cows)
# While Loop

Score = 500
while Score > 100:
    Score = int(input("enter a score: "))
    # if Score > 100 or Score < 0:
    #     print("Not a valid score, try again")

# if Score >= 85:
#     print("Distinction")
# elif Score >= 65:
#     print("Pass")
# else:
#     print("Fail")


# QA Exercise Names

# count = 0
# a   name = str(input("What is your name? "))
# while count < 5:
#     print(name, "is awesome")
#     count += 1

# name1 = input("enter your name: ")
# name2 = input("enter your name: ")
# name3 = input("enter your name: ")
# name4 = input("enter your name: ")
# name5 = input("enter your name: ")
count = 0
friends = []

while count < 5:
    name = input("enter your name: ")
    friends.append(name)
    count += 1 

for friend in friends:
    print(friend, "is awesome")