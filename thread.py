import threading
from queue import Queue
import time

print_lock=threading.Lock()

def examplejob(worker):
	time.sleep(0.5)

	with print_lock:
		print(threading.current_thread().name, worker)

def threader():
	while True:
		worker=q.get()
		examplejob(worker)
		q.task_done()

q=Queue()

for x in range(10):
	t=threading.Thread(target=threader)
	t.daemon=True
	t.start()

start=time.time()

for worker in range(20):
	q.put(worker)

q.join()
print("Entire job took:", time.time()-start)

print("\n")

#another example#easier to understand
class Messenger(threading.Thread):#inheriting from threading.Thread
	def run(self):#need to have this function#runs when thread is created
		for _ in range(10):#_ can be used when don't care about the loop number
			print(threading.currentThread().getName())#we can give every thread a name(default property) #prints name of the thread

x=Messenger(name="Send Message")#giving names to threads
y=Messenger(name="Receive Message")
y.start()
x.start()#runs the "run" function in the class #kicks off a thread 
#in the output, we can see that both the threads are executing simultaneously
#the processes are not waiting for each other to complete
#run the program several times if you don't see it at first
#do not use threads if there is calculation involved