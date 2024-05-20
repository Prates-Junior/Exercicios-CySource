import threading

def contador(l):
    for i in range(10000):
        with l:
            print(i)

lock = threading.Lock()
for i in range(100):
    t = threading.Thread(target=contador,args=(lock,))
    t.start()




