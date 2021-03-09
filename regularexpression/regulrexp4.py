#first charcter include A to k
#second must be a number and divisible by 3
#followed by any number of charcters

from re import *
rule='[a-k][369][a-zA-Z0-9]*'

varname=input("var name?")
matcher=fullmatch(rule,varname)
if matcher==None:
    print("variable not found")
else:
    print("variable found")