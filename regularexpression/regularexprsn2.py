from re import *
#predefined character set
#pattern="[ab]" #check for either a or b
#pattern="[a-z]" #check lower case  a to z
#pattern="[A-Z]" #check upper case  A to Z
#pattern="[a-b]" #check lower case  a to b
#pattern="[a-zA-Z]" #check low and upper a to z
#pattern="[0-9]" #check all digits
#pattern="[^0-9]" #check except all digit
#pattern="[a-zA-Z0-9]" #check all words
#----------------------------------

#predefined characters
#pattern="/s" #check spaces
#pattern="/w" #check words no special characters
#pattern="/W" #check except words with special characters
#pattern="/d" #check for digit 0 to 9
pattern="/D" #check for except digit 0 to 9






matcher=finditer(pattern,"ab _7kqlak")
for m in matcher:
    print(m.start())
    print(m.group())
