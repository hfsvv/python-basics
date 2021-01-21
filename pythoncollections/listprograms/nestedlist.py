students=[
    [10,"ajay","bca",210],
    [11,"arun","mca",220],
    [12,"vinay","bca",230],
    [13,"varun","bca",240],
    [14,"karan","bca",250],
    [15,"adhi","bca",260],
]
#print(students[0][1])
#print num with total mark>240
#for stud in students:
    #if stud[3]>240:
        #print(stud[1])
#print name only
#for stud in students:
        #print(stud[1])
#print sum of total
#s=0
#for stud in students:
 #   s+=stud[3]
#print(s)
#calculate total of bca and mca
mtotal,btotal=0,0
for stud in students:
    if stud[2]=="bca":
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
print("mca total=",mtotal)
print("bca total=",btotal)