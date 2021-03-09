size=int(input("Enter the size of stack"))
top=0
n=1
stk=[]
def push():
    item=int(input("enter the item"))
    global top
    if top<size:
        stk.insert(top,item)
        top+=1
    else:
        print("stack overflow")

def pop():
    global top
    top-=1
    if top<0:
        print("stack is empty")
    else:
        print(stk[top]," poped out")





def display():
    for i in range(0,top):
        print(stk[i])
while n!=0:
    option=int(input("enter the option 1:push, 2:pop ,3:display" ))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    n=int(input("do you want to continue press 0 for exist"))