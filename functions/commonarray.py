arr=[1,2,3,4,5,6,7]
arr1=[3,7,8,9]
#arr2=[]
# for a in arr:
#     for b in arr1:
#         if a==b:
#             arr2.append(a)
#             print(a)
#         else:
#             pass
comm=list(filter(lambda a:a in arr1,arr))
print(comm)