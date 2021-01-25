f=open("rept","r")
dict={}
for ch in f:
    words=ch.rstrip("\n").split(" ")
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,v)

#val=sorted(dict,key=dict.get,reverse=True)
#print(val[0])
