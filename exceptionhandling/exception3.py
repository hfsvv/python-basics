n1=int(input("n1"))
n2=int(input("n2"))
try:
    r = n1 / n2
    print("res=", r)
except:
    n2 = int(input("n2"))
    try:
        r = n1 / n2
        print("res=", r)
    except:
        n2 = int(input("n2"))
        r = n1 / n2
        print("res=", r)
finally:
    print("i have database transaction")
    print("i have file opn")


