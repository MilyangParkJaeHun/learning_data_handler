from multiprocessing import Process, Value, Array, Lock
import time
def f(l, n, a, idx):
    n.value = 3.1415927
    for j in range(3):
      l.acquire()
      try:
        n.value += 1
      finally:
        l.release()
      print(idx, " ", n.value)
         

if __name__ == '__main__':
    lock = Lock()
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(lock, num, arr, 0))
    p.start()
    time.sleep(1)
    p2 = Process(target=f, args=(lock, num, arr, 1))
    p2.start()
    
    p.join()
    p2.join()

    print(num.value)
    print(arr[:])
