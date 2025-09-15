class BMW():
    def mamimummspeed(self):
        print("The maximum speed of the BMW is 150")
    def mileage(self):
        print("The mileage of BMW is 12")
    def colour(self):
        print("The colour of the BMW is white")
class Ferrari():
    def mamimummspeed(self):
        print("The maximum speed of the Ferrari is 250")
    def mileage(self):
        print("The mileage of Ferrari is 32")
    def colour(self):
        print("The colour of the Ferrari is red")
obj=BMW()
obj2=Ferrari()
for car in (obj,obj2):
    car.mamimummspeed()
    car.mileage()
    car.colour()