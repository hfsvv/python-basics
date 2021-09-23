# Task2

import re

pawd=input("Enter password")
pawd=pawd.split(",")

ac=[]
for i in pawd:

    if len(i)<6 or len(i)>12:
        continue

    elif not re.search("([a-z])+",i):
        continue

    elif not re.search("([A-Z])+",i):
        continue

    elif not re.search("([0-9])+",i):
        continue

    elif not re.search("([$#@])+", i):
        continue

    else:
        ac.append(i)

print(ac)