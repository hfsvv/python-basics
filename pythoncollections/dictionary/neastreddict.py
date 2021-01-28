employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"john","salary":30000,"exp":2},
    1002:{"id":1002,"name":"peter","salary":35000,"exp":2},
    1003:{"id":1003,"name":"jack","salary":30000,"exp":2},
}
#nested dictionary
def printemp(**kwargs):
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass
    else:
        print("employee doewsnt exist")
printemp(id=1000,prop="salary")
    #nested dictionary
# print(employee[1000])
#
# #print name of employee who have id 1001
# if 1001 in employee:
#     print(employee[1001]["name"])
# else:
#     print("employee not exist")
#
# #print salary of employee who have id 1002
# if 1002 in employee:
#     print(employee[1002]["salary"])
# else:
#     print("employee not exist")
