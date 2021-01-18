lst=[10,8,7,12,11,5,6]
flag=0
#element 12
#step 1 sort
#[5,6,7,8,10,11,12]
# 0,1,2,3,4, 5, 6
# #l    m        u
#calculate mid=low+upper//2=3
#if element>list[mid] :12> 8:low=mid+1 4+6//2=5
#if element>list[mid] 12>11 low=mid+1=6
#mid=6+6//2=6
#elemnt>ist[mid 12>12
#elemnt<list[mid 12<12
#element=list[mid]12=12 element found
lst.sort()
low=0
upp=len(lst)-1
element=int(input("enter the element to seach"))
while(low<=upp):
    mid=(low+upp)//2
    if element>lst[mid]:
        low=mid+1
    elif element<mid:
        upp=mid-1
    elif element==lst[mid]:
        flag+=1
        break
if flag==0:
    print("element is not found")
else:
        print("element is found")

