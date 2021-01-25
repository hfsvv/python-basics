std = set()
fail = set()
word=[]
words=[]
s = open("students", "r")
f = open("fail", "r")
for line in f:
    word.append(line.rstrip("\n"))
for line in s:
    words.append(line.rstrip("\n"))

std.update(words)
fail.update(word)
fstd = std.intersection(fail)
print(fstd)
