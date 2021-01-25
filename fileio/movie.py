f=open("movies.csv","r")
#year wise movie count find
#highest movie count year
dict={}
dict2={}
for words in f:
    data=words.rstrip("\n").split(",")
    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict)
order=sorted(dict,key=dict.get,reverse=True)
print(order[0],dict.get(order[0]))
dict2=sorted(dict,reverse=True)
print(dict2)