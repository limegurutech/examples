import threading
import time

def say_hello_function1():
    for i in range(1,10):
        print("Hello Function 1")
        time.sleep(0.2)

def say_hello_function2():
    for i in range(1,10):
        print("Hello Function 2")
        time.sleep(0.2)

# say_hello_function1()
# say_hello_function2()

t1 = threading.Thread(target=say_hello_function1)
t2 = threading.Thread(target=say_hello_function2)

t1.start()
t2.start()

t1.join()
t2.join()




    
