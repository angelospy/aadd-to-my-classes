class pet:
    def __init__(self, name, a, h, p):
        self.name = name
        self.age = a
        self.hunger = h
        self.playful = p

    def getname(self):
        return self.name
    
    def getage(self):
        return self.age

    def gethunget(self):
        return self.hunger
    
    def getplayful(self):
        return self.playful

    #sets    sets cange the previus string or input

    def setname(self,xname):
        self.name = xname

    def setage(self,age):
        self.age = age
    
    def sethunger(self,hunger):
        self.hunger = hunger

    def setplayful(self,play):
        self.playful = play

pet1 = pet('gim',3,False,True)

print(pet1.getname())
print(pet1.getplayful())

pet1.setname('snowbal')

print(pet1.getname())

print(pet1.name)

pet1.name = 'jim'

print(pet1.name)


#class dog:
#    def __init__(self):
#        pet.__init__(self)
    