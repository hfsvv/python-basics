lst=[8,2,4,3,9,7,2,1,6]
lst.sort()
pair=int(input("enter the pair"))
low=0
upp=len(lst)-1
while(low<upp):
    tot=lst[upp]+lst[low]
    if(pair==tot):
        print(lst[low],lst[upp])
        break
    #else:
     #   low+=1
    #if(low==upp-1):
     #   upp-=1
      #  low=0
    elif(tot<pair):
        low += 1
    elif(tot>pair):
        upp-=1




#n=int(input("enter the range of list"))
#lst=list()
#for i in range(0,n):
 #   number=int(input("enter the number"))
  #  lst.append(number)
#num=int(input("enter the number to find pair"))
#for x in range(0,len(lst)):
 #   for y in range(x+1,len(lst)):
  #      if lst[x]+lst[y]==num:
   #         print(lst[x],lst[y])
