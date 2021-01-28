f=open("covid_19_india1.csv","r")
cvd={}
for line in f:
    data = line.rstrip("\n").split(",")
    state = data[3].rstrip("***")
    if state == "Telengana":
        state = "Telangana"
    cvd[state]={}
    confirmed_case = int(data[8])
    cured_case = int(data[6])
    cvd[state]["Name"]=state
    if state not in cvd:
        cvd[state]["confirmed cases"] = confirmed_case
        cvd[state]["cured cases"] = cured_case
    else:
        cvd[state]["confirmed cases"] = confirmed_case
        cvd[state]["cured cases"] = cured_case
print(cvd)

def printdt(**kwars):
    st=kwars["state"]
    if st in cvd:
        print(cvd[st]["Name"])
        if "prop" in kwars:
            prop=kwars["prop"]
            print(cvd[st][prop])
        else:
            pass
    else:
        print("state not exist")
printdt(state='Kerala',prop="confirmed cases")

#     st=kwargs["state"]
#     if st in cvd:
#          print(cvd[state]["Name"])
#           if ("prop" in kwargs):
#                 prop=kwargs["prop"]
#             print(cvd[state][prop])
#          else:
#              pass
#     else:
#          print("State is not found")
# printdt(state="Kerala")
#
#

