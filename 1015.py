#Distância Entre Dois Pontos
#Splitei 2 vezes separadamente pq a questao da duas entradas em cima e duas em baixo.
import math
x1, y1 = str(input()).split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = str(input()).split()
x2 = float(x2)
y2 = float(y2)

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 

print(f'{distancia:.4f}')