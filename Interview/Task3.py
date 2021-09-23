# n=4
# c=1
# s=[1,2]
# for x in range(0,1):
#     for y in range(1,x):
#         print(s[x])
#         k=(y*y)+1
#         s[x+1]=k
#
#
#
#
#
#
#
#
#     print()

n=6
num=1
for i in range(0,n):
    num=1
    for j in range(1,i+1):
        print(num,end=" ")
        num=(j*j)+1
    print('')
