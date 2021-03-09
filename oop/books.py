#operator overloading

class book:
    def __init__(self,page):
        self.page=page
    def __add__(self, other):
        return book(self.page+other.page)
    def __mul__(self, other):
        return book(self.page*other.page)
    def __sub__(self, other):
        return book(self.page-other.page)
    def __str__(self):
        return str(self.page)
obj=book(100)

obj1=book(200)
obj2=book(700)

print(obj+obj1+obj2)

print(obj-obj1-obj2)

print(obj*obj1*obj2)