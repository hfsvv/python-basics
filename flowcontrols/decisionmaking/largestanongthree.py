#read three numbers and find highest number
#find second largest number 40
#sort these three numbers 30 40 50
num1=int(input("enter num1"))#50
num2=int(input("enter num2"))#40
num3=int(input("enter num3"))#

if (num1 > num2)&(num1 > num3):
    print("num1 is highest")
    #num1 is the highest number in this code block
    #possibilty for second largest num either num2 or num3
    if(num2>num3):
        print(num1,num2,num3)
    elif(num3>num2):
        print("num3 is second largest",num1,num3,num2)

elif (num2>num1)&(num2>num3):

    if (num1> num3):
        print("second largest is num1", num1)
    else:
        print("num3 is second largest", num3)

elif (num3 > num1)&(num3 > num2):
    if (num1 > num2):
        print("second largest is num1", num1)
    else:
        print("num2 is second largest", num2)


elif (num1 == num2)&(num1 == num3):
    print("3 numbers are equal")