import threading
import time
def worker_1():
	while True:
		time.sleep(3)
		print("Hello from worker 1")

		
def worker_2():
	while True:
		time.sleep(5)
		print("Hello from worker 2")

		
thread_1 = threading.Thread(target=worker_1)
thread_2 = threading.Thread(target=worker_2)


def run():
    thread_1.start()
    thread_2.start()
    

run()
