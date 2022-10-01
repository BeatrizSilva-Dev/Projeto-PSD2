import threading
import multiprocessing
from threading import Thread
from datetime import datetime
from multiprocessing import Process
antes = datetime.now()
print("Antes = ", antes)



arq = open('1024.txt', 'r')  
texto = []  
matriz = [] 
texto = arq.readlines() 

 

for i in range(len(texto)):          
    matriz.append(texto[i].split())

matriz.pop(0)
for x in range (len(matriz)):
   for y in range(len(matriz[0])):
    matriz[x][y] = float(matriz[x][y]) 
    
tamanhodamatriz = len(matriz)
qntdthreads = multiprocessing.cpu_count()*2 
divisaoDaThread = tamanhodamatriz/qntdthreads
matRes = []

def multiplicarMatriz(i, divisaoDaThread,mult):
    for j in range(int(i*divisaoDaThread), int(divisaoDaThread*mult)):
        for k in range(int(len(matriz[0]))):
            v= 0
            for l in range(int(len(matriz[0]))): 
                v+=matriz[j][l]*matriz[l][k]
            matRes[j].append(v)
    return matRes

mult = 1
for i in range(len(matriz)):
    matRes.append([])
for i in range(qntdthreads):
    th1 = threading.Thread(target=multiplicarMatriz, args=[i, divisaoDaThread, mult]) 
    if __name__ == '_main_': 
        Process(target=multiplicarMatriz, args=[i, divisaoDaThread, mult])
    th1.start() 
    th1.join() 
    mult+=1

print(matriz)
print("\n---------------------------------------------------------------\n")
print(matRes)

depois = datetime.now()
print("Depois = ", depois)
print(depois - antes)


with open('matrizesp3.txt', 'a') as arquivo:
    arquivo.write('Matriz : ')
    arquivo.write(str(matRes))
    arquivo.write('\n')
    arquivo.write('Linhas: ')
    arquivo.write(str(len(matriz)))
    arquivo.write('\n')
    arquivo.write('Colunas: ')
    arquivo.write(str(len(matriz[0])))
    arquivo.write('\n')
    arquivo.write('Cores : ')
    arquivo.write(str(qntdthreads))
    arquivo.write('\n')
    arquivo.write('Tempo Inicial : ')
    arquivo.write(str(antes))
    arquivo.write('\n')
    arquivo.write('Tempo Final : ')
    arquivo.write(str(depois))
