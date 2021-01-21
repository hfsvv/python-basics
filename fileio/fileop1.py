#read
#write
#append
#step 1 we have to create reference
#fopen("filepath","mode")
word=[]

f=open("demo","r")
for line in f:
    word.append(line.rstrip("\n").split(" "))
print(word)
mywords=[]
for lst in word:
    for wrd in lst:
        mywords.append(wrd)
print(mywords)

#print stud name who fails:set
#highest repeating word from list:dict