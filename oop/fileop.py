#print employee details whose ndesig developer
#no of employee as dev
#print employee details have highest salary
t=0
class employee:
    def __init__(self,eid,name,desig,exp,salary,):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary
    def __str__(self):
        return self.name

f=open("employee.txt","r")
emplist=[]
sallist=[]
s=[]
for lines in f:
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(employee(eid,name,desig,exp,salary))
# for employee in emplist:
#     print(employee)
# for employee in emplist:
#     print(employee)
# for employee in emplist:
#     sallist.append(employee.salary)
# h=max(sallist)
# for employee in emplist:
#     if employee.salary==h:
#         print(employee,"has highest salary",h)
# for employee in emplist:
#     if employee.desig=="Developer":
#         s.append(employee.salary)
#         t+=1
#         print("Developers\n",employee)
#         print(t)
#
# l=min(s)
# for employee in emplist:
#     if employee.desig ==  "Developer":
#        if employee.salary==l:
#             print(employee,"has lowest salary",l)

#print employee details whose ndesig developer
dev=list(filter(lambda emp:emp.desig=="Developer",emplist))
for emp in dev:
    print(emp)
cnt=len(list(filter(lambda emp:emp.desig=="Developer",emplist)))
print(cnt)

high=max(list(map(lambda emp:emp.salary,emplist)))
print(high)
low=min(list(map(lambda emp:emp.salary,emplist)))
print(low)
