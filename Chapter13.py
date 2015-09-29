#NOTE: Chapter 13 exercises (to review again!)

#No. 1
class Food(object):
    def __init__(self,name,veg,meat,weight):
        self.name = name
        self.veg = veg
        self.meat = meat
        self.weight = weight
    def new_weight(self,lbs):
        self.weight+=lbs
steak= Food("steak",False,True,20)

steak.new_weight(3)

print steak.weight

#NO. 2
class Animals(object):
    def __init__(self,name,cat,dog,energy):
        self.name = name
        self.cat = cat
        self.dog = dog
        self.energy = energy
    def mammal(self,sleep): #NOTE: defines what you call
        self.energy+=sleep
fido= Animals("Fido",False,True,100)
print fido.energy #NOTE: shows energy level at 100. 
fido.mammal(20)

print fido.energy

#No. 3
class Plant(object):
    def __init__ (self,name,typeof,bloomed):
        self.name = name
        self.typeof = typeof
        self.bloomed = bloomed
    def flower(self): 
        self.bloomed=True #NOTE: For each object that passes thru the flower function, we want it to be True.
rose= Plant("Queen Mary","flower",False) #Note: Rose is the variable the value is the object.
print rose.bloomed
rose.flower()
print rose.bloomed


