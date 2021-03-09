import threading
import time

def display():
    for i in range(1,10):
        time.sleep(2)
        print("child thrad executing")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()
begint=time.time()
t.join()

for i in range(1, 10):
    time.sleep(2)
    print("main thrad executing")
print(threading.currentThread().getName())
endt=time.time()
total=endt-begint
print(total)