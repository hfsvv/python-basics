# cube=lambda num1:num1**3
# print(cube(3))
#
# even=lambda num:num%2==0
# print(even(6))

#map()

lst=[1,2,3,6,7,5]
# sqlist=list(map(lambda lst:lst**2,lst))
# # print(sqlist)
# res=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
# print(res)

# # filter
# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)
# odd=list(filter(lambda num:num%2!=0,lst))
# print(odd)

# names=["India","Usa","Uk","srilanka","argentina"]
# upp=list(map(lambda str:str.upper(),names))
# print(upp)
#
# #print starting a
# acountry=list(filter(lambda str:str[0]=="a",names))
# print(acountry)
#
#reduce
from functools import reduce
lst1=[10,20,50,40]
sum=reduce(lambda num1,num2:num1+num2,lst1)
print(sum)
high=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst1)
print(high)