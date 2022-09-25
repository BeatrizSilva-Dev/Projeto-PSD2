#Matriz 1
arq = open('int.txt', 'r')  
texto = []  
matriz1 = [] 
texto = arq.readlines() 


for i in range(len(texto)):          
    matriz1.append(texto[i].split())

matriz1.pop(0)


#for i in range(len(texto)):          
#    print(matriz1[i])  

def getLinha(matriz, n):
    return [i for i in matriz[n]]  

def getColuna(matriz, n):
    return [i[n] for i in matriz]

mat1  = matriz1
