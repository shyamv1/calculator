from threading import Thread
import threading
import time 

def fun1():
		print ( "Starting the thread % s" % threading.currentThread().getName())
		time.sleep(3)
		print ("exiting the thread %s" %threading.currentThread().getName())

def fun2():
		print ( "Starting the thread % s" % threading.currentThread().getName())
		time.sleep(2)
		print ("exiting the thread %s" %threading.currentThread().getName())

def fun3():
		print ( "Starting the thread % s" % threading.currentThread().getName())
		time.sleep(1)
		print ("exiting the thread %s" %threading.currentThread().getName())

Thread(target=fun1).start()
Thread(target=fun2,name='fun2').start()
Thread(target=fun3,name='fun3').start()