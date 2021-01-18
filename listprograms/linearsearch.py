lst=[10,11,12,13,14,15,16]
key=int(input("enter the number to search"))
flag=0
cnt=0
for num in lst:
    if num==key:
        flag+=1
        break
    else:
        pass
    cnt+=1
if flag==0:
    print("element is not found")
else:
    print("element is found at",cnt)

