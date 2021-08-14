from math import sqrt
import random
from estado import Nodo
from queue import PriorityQueue

matriz_objetivo = {}
matriz_inicial = {}


def generarNodoObjetivo():
    valor = 1
    for x in range(1,N+1):
        for y in range(1,N+1):
            if x == 1 and y == 1:
                matriz_objetivo[""] = { "row": 1, "col": 1}
            else:
                matriz_objetivo[valor] = { "row": x, "col": y}
                valor += 1 


def generarEstadoInicial():
    valores = list(range(1,N*N)) + [""] 
    rand = random.sample(valores, N*N)
    print("Estado inicial:", rand)
    count = 0
    for x in range(1,N+1):
        for y in range(1,N+1):
            matriz_inicial[rand[count]] = { "row": x, "col": y}
            count += 1 
    verificarMatrizAleatorio(rand)


def verificarMatrizAleatorio(v):
    solucionable = inversion(v)
    if solucionable:
        init_search()
    else:
        print("Esta matriz inicial no puede ser resuelta")


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
        
        if comparar(nodo.matriz, matriz_objetivo) == True:
            s = nodo.solucion()
            print("Camino de la solucion:", s)
            break          
        else:
            if verificarEstadoRepetido(explorado, nodo.matriz) != True:
                explorado.append(nodo.matriz)
                counter = nodo.expandir(prioridad, N, matriz_objetivo, counter) 
    print("Cantidad de Nodos visitados:",len((explorado)))



def verificarEstadoRepetido(explorado, matriz):
    ban = False
    for m in explorado:
        if comparar(m, matriz) == True:
            ban = True
            break
    return ban            


def comparar(matriz_x, matriz_y):
    flag = True
    for key in matriz_objetivo.keys():
        if matriz_x[key]["row"] != matriz_y[key]["row"]:
            flag = False
            break 
        elif matriz_x[key]["col"] != matriz_y[key]["col"]:
            flag = False
            break
    return flag         

N = int(input("N-Puzzle: "))
generarNodoObjetivo()
generarEstadoInicial()
#print(matriz_inicial)
#init_search()