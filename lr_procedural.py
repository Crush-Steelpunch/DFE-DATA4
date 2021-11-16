def leon_does_a_test(inputvar):
    print(inputvar)
    if inputvar < 5:
        exit()


x = 1000
y = 2000
z = x * y
leon_does_a_test(z)
z = y - x
leon_does_a_test(z)
z = y * (x/2)
leon_does_a_test(z)
z = x * x
leon_does_a_test(z)
z = y * y
leon_does_a_test(z)
