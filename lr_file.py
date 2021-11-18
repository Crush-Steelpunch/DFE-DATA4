myfile = open('README.md')
chars = myfile.readlines()
myfile.close()


chars.insert(2,"I like files\n")
chars.append("\nCheese is pretty good to eat\n")
print(chars)
output = "".join(chars)



myfile = open('README.md',mode='w')
myfile.write(output)
myfile.close()