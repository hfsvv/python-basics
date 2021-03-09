from functools import reduce
employees=[
    {"id":10,"name":"christ","desig":"data analyst","sal":50000,"join":1989,"resign":1992},
    {"id": 11, "name": "jerry", "desig": "develop", "sal": 70000, "join": 1979, "resign": 1999},
    {"id": 12, "name": "febin", "desig": "data analyst", "sal": 40000, "join": 1989, "resign": 2001}

]
ex=[]
#highest salary
#experience> 10
for emp in employees:
    high=max(list(map(lambda emp:emp["sal"],employees)))
    ex.append(emp["resign"]-emp["join"])
    exp=list(filter(lambda n1:n1>10,ex))
print(exp)
    #     print(emp)
for emp in employees:
 if emp["sal"]==high:
     print(emp)
#highest points
#lowest point
#highest goal scored