size=int(input("enter the size of queue"))
que=[]
rear=0
front=0
n=1

def insert():
    item=int(input("Enter the item to enter"))
    global rear
    if rear<size:
        que.insert(rear,item)
        rear+=1
    else:
        print("queue is full")

def deletion():
    global front
    if front==rear:
        print("queue is empty")
    else:
        print(que[front],"is deleted")
        front+=1


def display():
    for i in range(front,rear):
        print(que[i])



while n!=0:
    opt=int(input("Enter the option 1:insertion 2:deletion 3:display"))
    if opt==1:
        insert()
    elif opt==2:
        deletion()
    elif opt==3:
        display()
    else:
        print("invalid option")
    n = int(input("do you want to continue press 0 for exist"))