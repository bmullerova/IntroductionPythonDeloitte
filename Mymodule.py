class Animal(object):
    def __init__(self, startname, age):
        self.name = startname #attribute 1
        self.age = age #attribute 2
    def desctription(self): #method
        print("this is " + self.name)
        print("he/she is " + str(self.age) + " years old")


