def stock_stuff(inputvar):
    productcodelen = len(inputvar)
    return productcodelen




product_code = input("What do you want to buy?")

returnvar = stock_stuff(product_code)

print("Your product code was", returnvar,"chars long")
