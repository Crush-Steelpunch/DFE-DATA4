class Budget:

    def __init__(self):
        self.balance = 0.0

    def deposit(self,moneyin):
        self.balance += moneyin

    def withdraw(self,moneyout):
        self.balance -= moneyout
    
    def transferto(self,account,value):
        self.withdraw(value)
        account.deposit(value)
    



food = Budget()
clothes = Budget()
house = Budget()

food.deposit(100)
food.withdraw(1.99)
print("food", food.balance)
food.transferto(clothes, 30)
print("food:", food.balance)
print("clothes:",clothes.balance)
clothes.transferto(house, 15)
print("clothes:",clothes.balance)
print("house:",house.balance)
total = 0
for i in [food,clothes,house]:
    total += i.balance
print(total)