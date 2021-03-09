#validphone
from re import *
regno=input("enter email")
rule='[a-z.]*[/d]*@gmail.com'

matcher=fullmatch(rule,regno)
if matcher==None:
    print("invalid mobno")
else:
    print("valid mob no")