# class template for dog object 
class Dog:
    #initialisation method, gets run whenever we create a new dog
    # the self just allows this function to reference variables relevant to this particular dog
    def __init__(self,name,hungerLevel):
        self.name = name
        self.hungerLevel = hungerLevel

    # query the status of the dog
    def status(self):
        print("Dog is called",self.name)
        print("Dog hunger level is",self.hungerLevel)
        pass

    # set the hunger level of the dog
    def setHungerLevel(self, hungerLevel):
        self.hungerLevel = hungerLevel
        pass

    # dogs can bark
    def bark(self):
        print("Woof!")
        pass

# create two dog objects
# note that we don't need to include the delf from the parameter is
lassie = Dog("lassie","Mild")
yoda = Dog("Yoda","Ravenous")

# check on Yoda & Lassie
yoda.status()
lassie.status()

# get Lassie to bark
lassie.bark()

# feed Yoda
yoda.setHungerLevel("Full")
yoda.status()

