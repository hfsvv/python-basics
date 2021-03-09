lst=[[10,20],[30,40],[50,60]]

ls=[num for l in lst for num in l]
print(ls)

# ls=[]
# for l in lst:
#     for n in l:
#         ls.append(n)


#sq=list(map(lambda num:num**2,lst))
# sq=[num**2 for num in lst]
# print(sq)