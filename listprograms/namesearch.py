lst=["tcs","wipro","cts","ust"]
cname=input("enter company name")
flag=0
for com in lst:
    if(cname==com):
        flag+=1
        break
    else:
        pass
if flag==0:
    print("element is not found")
else:
        print("element is found")

