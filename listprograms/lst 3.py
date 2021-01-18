lst=[10,11,12,13,14,15,16]
evelist=list()
oddlist=list()
for num in lst:
    if num%2==0:
        evelist.append(num)

    else:
        oddlist.append(num)

print(evelist)
print(oddlist)