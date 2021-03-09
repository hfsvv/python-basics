class students:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
obj=students(101,"Akshay","django",140)
obj1=students(102,"Ajay","mean",180)
obj2=students(103,"Adhil","django",160)
obj3=students(104,"Arun","mean",170)
slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
slist.append(obj3)
t=0
for stud in slist:
    if stud.course=="django":
        print(stud.name)
        t+=1
        #total djangp
print(t)