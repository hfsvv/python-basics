#print[18,15,14,13]
#total-number
#inputing list


lists=[2,5,6,7]
total=sum(lists)
out=list()
for i in lists:
    out.append(total-i)
    #print(total-i)
print(out)