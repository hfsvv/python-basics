#polymorphism
#more than one form
#method overloading
#method overriding
#operator overloading


#method oveeloading
#same method with diff arguments
#not possible work recently implement
class maths:
    def add(self):
        print("inside no arg")
    def add(self,num1):
        print("inside 1 arg")
    def add(self,num1,num2):
            print("inside 3 arg")

m=maths()
m.add()