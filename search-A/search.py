from math import sqrt
import random
from estado import Nodo
from queue import PriorityQueue 
from datetime import datetime

matriz_objetivo = {}
matriz_inicial = {}


def generarNodoObjetivo():
    valor = 1
    for x in range(1,N+1):
        for y in range(1,N+1):
            if x == N and y == N:
                matriz_objetivo[""] = { "row": N, "col": N}
            else:
                matriz_objetivo[valor] = { "row": x, "col": y}
                valor += 1 

#
def generarEstadoInicial():
    valores = list(range(1,N*N)) + [""]
    solucionable = False
    while not solucionable: 
        rand =  random.sample(valores, N*N)
        count = 0
        for x in range(1,N+1):
            for y in range(1,N+1):
                matriz_inicial[rand[count]] = { "row": x, "col": y}
                count += 1 
        solucionable = inversion(rand) 
    print("Estado inicial:", rand)
    return matriz_inicial, rand


def inversion(vector):
    count = 0
    for i in range(0,len(vector)-1):
        for j in range(i+1, len(vector)):
            if (vector[i] != "" and vector[j] != "" and vector[i] > vector[j]):
                count += 1
    return count % 2 == 0


def init_search():
    explorado = []
    prioridad = PriorityQueue()
    raiz = Nodo(matriz_inicial, None, 0, None)
    raiz.distancia_manhattan(matriz_objetivo)
    counter = 0
    prioridad.put((raiz.costo_f, counter, raiz))
    while not prioridad.empty():
        item = prioridad.get()
        nodo = item[2]
        
        if nodo.matriz == matriz_objetivo:
            s = nodo.solucion()
            print("Camino de la solucion:", s)
            break          
        else:
            if nodo.matriz not in explorado:
                explorado.append(nodo.matriz)
                counter = nodo.expandir(prioridad, N, matriz_objetivo, counter) 
    print("Cantidad de Nodos visitados:",len((explorado)))


N = int(input("N-Puzzle: "))
generarNodoObjetivo()
start = datetime.now()
generarEstadoInicial()
init_search()
end = datetime.now() - start
print("Tiempo de solucion: ", end)
