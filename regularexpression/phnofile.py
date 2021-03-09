from re import *
f=open("phno","r")
lst=[]
for ph in f:
    lst.append(ph.rstrip("\n"))
print(lst)
rule='\d{10}'
for p in lst:
    matcher=fullmatch(rule,p)
    if matcher==None:
        print(p, " is invalid mobno")
    else:
        print(p," is valid mob no")