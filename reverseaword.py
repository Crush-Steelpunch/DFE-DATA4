#  Write a Python program that accepts a word from the user
# and reverse it


userWord = input("wrdin: ")  # accept a word from the user

# Q: do we know how many letters?  NO
# Q: is there way of finding out how many letters were entered?  len()

letterCount = len(userWord)

# Q: Now I know how many letters. Can I loop? Which loop?

revWord = ""
for i in range(letterCount-1,-1,-1):
    revWord = revWord + userWord[i]

print(revWord)


#revWord = userWord[::-1]