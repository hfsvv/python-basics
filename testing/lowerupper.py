num=int(input("enter number"))
upp=int(input("enter upper"))
low=int(input("enter lower"))
for i in range(1,upp+1):
    if i**num in range(low,upp):
        print(i**num)
    else:
        pass
