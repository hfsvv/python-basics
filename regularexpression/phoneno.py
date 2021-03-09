#validphone
from re import *
regno=input("enter mob no")
rule='\d{10}'

matcher=fullmatch(rule,regno)
if matcher==None:
    print("invalid mobno")
else:
    print("valid mob no")