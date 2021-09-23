k=int(input())
if not k%2==0:

    row=int(k/2)
    k=2*row-2
    for i in range(0,row):
        for j in range(0,k):
            print(end=" ")
        k-=1
        for j in range(0,i+1):
            print("*",end=" ")
        print("")
    k=row-2
    for i in range(row,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k+=1
        for j in range(0,i+1):
            print("*",end=" ")
        print("")
