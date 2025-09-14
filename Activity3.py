#class 1
class india():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most spoken language in India")
    def type(self):
        print("India is a devoloping country")

#class 2
class USA():
    def capital(self):
        print("Washington D.C is the capital of USA")
    def language(self):
        print("English is the most spoken language in USA")
    def type(self):
        print("USA is a devoloped country")
# object creation
obj1=india()
obj2=USA()


#common interface
for country in (obj1,obj2):
    country.capital()
    country.language()
    country.type()