emp={"id":100,"ename":"ajay","exp":2,"salary":5454}
if "salary" in emp:
    print(emp["salary"])
print(emp["ename"])
if "gender" in emp:
    print("exit")
else:
    emp["gender"]="MALE"
print(emp)
#if emp salary <6000 add 500 more
if emp["salary"]<6000:
    emp["salary"]+=500
print(emp)