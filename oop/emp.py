class emp:
    def __init__(self,eid,name,designation,salary): #constructor
        self.eid=eid
        self.name=name
        self.desg=designation
        self.salary=salary

    def printemp(self):
        print("id= ",self.eid,"name= ",self.name,"designation =",self.desg,"salry= ",self.desg)

obj=emp(100,"ajay","developer",25000)#constructor calling


obj.printemp()
