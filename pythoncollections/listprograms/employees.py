employees=[
    [10,"christy","data analyst",50000],
    [11,"john","ba",60000],
    [12,"jacob","data analyst",40000],
    [13,"sab","developer",40000],
    [14,"johny","developer",90000],
    [15,"tom","developer",30000],
]
#print employees in company
nofemp=len(employees)
print(nofemp)
#print how musch salary company make in month end
total=0
for emp in employees:
    total+=emp[3]
print(total)
#how many job section
danal,dba,ddvlpr=0,0,0
for emp in employees:
    if emp[2]=="ba":
        dba+=1
    elif emp[2]=="data analyst":
        danal+=1
    else:
        ddvlpr+=1
print("ba=",dba,"analyst=",danal,"developer",ddvlpr)
#print highest salaried employeee
salary=[]
for emp in employees:
    salary.append(emp[3])
h=(max(salary))
print(h)
for emp in employees:
    if emp[3]==h:
        print(emp)

#print emplo        yee who has low salary in developer
m=min(salary)
for emp in employees:
    if (emp[3]==m) & (emp[2]=="developer"):
        print(emp)
