class parent:   #class parent(object)
    def phone(self):
        print("i have nokia 105")
    def __str__(self):    #method overriding
        return "hello world"
c=parent()
c.phone()
print(c)