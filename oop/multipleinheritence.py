class parent:
    def phone(self):
        print("inside parents")
class child():
    def m1(self):
        print("inside child")
class subchild(child,parent):
    def m2(self):
        print("inside subchild")
c=subchild()
c.phone()
c.m1()
c.m2()
