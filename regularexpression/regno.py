#valid vehicle regno
from re import *
regno=input("enter reg no")
rule='KL[0-9]{2}[A-Za-z]{2}[0-9]{4}'

matcher=fullmatch(rule,regno)
if matcher==None:
    print("invalid regno")
else:
    print("valid reg no")