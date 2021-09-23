# # Task 4
n=9
sp=0
pp=0
st=int(n/2+1)
pt=st
if (n%2!=0)&(n>0):
    for i in range(1,int(n/2+2)):
        for j in range(1,sp+1):
            print(" ",end="")
        for k in range(1,st+1):
            print("*",end=" ")
        print('')
        pp+= 1
        pt-= 1
        sp+=2
        st-=2
    pp-=1
    pt+=3
    for i in range(int(n/2+2),n):
        if (pp % 2 == 0):
            for j in range(1,pp+1):
                print(" ",end="")
        if(pt%2!=0):
            for k in range(1,pt+1):
                print("*",end=" ")

        print()
        pp-=1
        pt+=1

