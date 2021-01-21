text="hai hello hai hello hy"

#o/p hai 2 hello 2
words=text.split(" ")
print(words)
#[hai ,hello ,hai ,hello]
dict={}

#key   value
#hai   1
#hello  1
for word in words:
    if (word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)