#quantifiers
from re import *
#pattern="a" single a
#pattern="a+" more than single a excluding zero no of a
#pattern="a*" more than single a including zero no of a
#pattern="a?" a present in every addres
#pattern="a{2}" #2 bo of a
pattern="a{2,4}" #min 2 and max 4 a
matcher=finditer(pattern,"aaaaabaaaabaa")
for match in matcher:
    print(match.start(),"=>",match.group())


    #common in two arrays

    #[1,2,3,4,5] [4,5,1,2,3]