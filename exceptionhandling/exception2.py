lst=[10,20,30]
pos=int(input("enter the position"))
n1=int(input())
n2=int(input())




try:

    r = n1 / n2
    print("res=", r)

    print(lst[pos])
except Exception as e:
    print(e.args)