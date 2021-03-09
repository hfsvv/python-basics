#regularexpression
#step 1 import re
from re import *
c=0
pattern="ab"
matcher=finditer(pattern,"abababababbbababa")
for m in matcher:
    print(m.start())
    print(m.group())
    c+=1
print(c)