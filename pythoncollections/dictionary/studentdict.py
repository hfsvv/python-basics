#printdata(roll=1000) print name of student with roll 1000
#printdata roll=1001 property =course print name,course
student=open("students","r")
students={}
for line in student:
    #roll,name,mark,course=line.rstrip("\n".split(",")
    #students[roll]={}
    #students[roll]={"roll":roll,"name":name,"mark":mark,"course":course}




    data=line.rstrip("\n").split(",")
    rol=int(data[0])
    students[rol]={}
    students[rol]["roll"] = data[0]
    students[rol]["name"]=data[1]
    students[rol]["mark"] = data[2]
    students[rol]["course"]=data[3]
print(students[1000])

def printdt(**kwargs):
    roll=kwargs["rol"]
    if roll in students:
        print(students[rol]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(students[rol][prop])
        else:
            pass

    else:
        print("Employee doesnt exist")
printdt(rol=1000,prop="mark")