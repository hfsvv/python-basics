num=int(input("enter number"))#123
res=0
while(num>0):#123>0 12>0 1>0 0>0
    digit=num%10#digit=123%10=3 12%10=2 1%10=1
    res=res+digit**3#res=0+3**3=27 #27+2**3=35 35+1=36
    num//=10#123//10=12 12//10=1 1//10=0
print(res)#36