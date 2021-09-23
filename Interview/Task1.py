# Task1

# lst=[]
# num=[x for x in input().split(',')]
# for p in num:
#     x=int(p,2)
#     if not x%5:

nums=list(input("enter 4 digit binary number").split(','))
res=[num for num in nums if not int(num,2)%5]
print(res)