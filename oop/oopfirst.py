#class
#object
#reference
class person:
    #methods
    def setperson(self,age,name):
        self.age=age #instancevariable
        self.name=name
    def printperson(self):
        print(self.age)
        print(self.name)
#class is person
#setperson()
#printperson
obj=person() #reference
obj.setperson(25,"ajay")
obj.printperson()   #objects

print(obj.age)


#instance variable are prepended with self keyword
#we can access instanc variable outside of class by ref
#inside class using selg

#employee
#eid,namemdesig,salary
#initialise
#create print
#have min 2 objects

#constructors
#initialising instance variable
#constructor name is always class name in java and cpp in python constructor name is__init__
#constructor automatically invoke in object creation
