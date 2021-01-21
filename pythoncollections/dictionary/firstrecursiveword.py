pattern="ARABIC"
#find first recursive character
dict={}
#for ch in pattern:
 #   if ch not in dict:#a is not in dict a:1
#        dict[ch]=1
#    else:
 #       print(ch,"is first recursive")
 #       break


 #print largest recursive character
for ch in pattern:
    if ch not in dict:#a is not in dict a:1
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
    print(key,",",value)
print(dict.get("R"))# to get value
data=sorted(dict,key=dict.get,reverse=True)
print(data[0])