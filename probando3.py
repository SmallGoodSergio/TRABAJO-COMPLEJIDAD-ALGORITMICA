import numpy as np



matriz = np.loadtxt("texto.txt",dtype=int)

print(matriz)

tamaño = 20


pared = [0] * 1
n = 0
print(pared[0])
for fila  in range(3):

    for columna in range(3):
        
        x = columna * tamaño
        y = fila * tamaño
        pared[n] = (x,y)
        print(x)
        print(y)
        pared.append(0)
        n+=1



print(pared)