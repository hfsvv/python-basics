expenses={"jan":3000,"feb":2500,"march":2800,"april":2500,"may":2200}
print(expenses["march"])
#value stored in dict as key and pair
#how do v fetch value from key
#key must be unique

#check key available
print("june" in expenses)

#adding new key
expenses["june"]=2900
print(expenses)

#updating value
expenses["march"]-=2700
print(expenses)