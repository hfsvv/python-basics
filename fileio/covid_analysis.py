f=open("covid_19_india.csv","r")

dict={}
for line in f:
    data=line.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telangana"
    confirmed_case=int(data[8])
    if state not in dict:
        dict[state]=confirmed_case
    else:
        dict[state] = confirmed_case
for k,v in dict.items():
    print(k,"=======>",v)
#most confirmed case
res=sorted(dict,key=dict.get,reverse=True)
print(res[0],dict.get(res[0]))
#alphabetical order state wise
res1=sorted(dict)