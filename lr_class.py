class Dog:

    # energy = "high"



    def __init__(self,inputenergy = "high"):
        self.energy = inputenergy


    def speak(self):
        print(getattr(self.energy)
        print("woof")
    
    def manyspeak(self):
        for i in range(5):
            self.speak()

    def total(self,x,y,z):
        return x + y + z

    # def __yipyipyip__(self,numofyips):
    #     for i in range(numofyips):
    #         print("yip")

    # def yips(self):
    #     self.__yipyipyip__(8)




havoc = Dog()

havoc.speak()
print(havoc.energy)

clifford = Dog("large")
clifford.speak()

print(clifford.total(3, 3, 3))

scooby = Dog("scared")
scooby.speak()

snoopy = Dog("Fighing the Red Baron")
snoopy.manyspeak()