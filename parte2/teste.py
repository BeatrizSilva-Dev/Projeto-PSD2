from threading import Thread
import time
import multiprocessing
import random
import sys

def pingPong(nome, tempo):
    vezes = 0
    while vezes <= 10:
        sys.stdout.write(" Thread Name: " + str(nome) + " Sleep: " + str(tempo) + " Vez: " + str(vezes) + "\n")
        sys.stdout.flush()
        vezes += 1        
        time.sleep(tempo)    

coress = multiprocessing.cpu_count()
print("Cores: ", coress)
print(range(coress))

threadBag = list()
# Com 2 Threads

for i in range(0,coress):
    print(i)
    threadBag.append(Thread(target=pingPong,args=[i, random.random()]))
    
for i in threadBag:
    i.start()