lst=[1,2,3,4,5,6]
s=0
#eveb or not
for n in lst:
    if n%2==0:
        print(n)
for i in range(0,len(lst)):
    print(lst[i])
# total sum
for n in lst:
    s=s+n
print(s)