from estado import Nodo
from queue import PriorityQueue 
from datetime import datetime


def generarMeta(n):
    valor = 1
    d = {}
    for x in range(1,n+1):
        for y in range(1,n+1):
            if x == n and y == n:
                d[""] = { "row": n, "col": n}
            else:
                d[valor] = { "row": x, "col": y}
                valor += 1 
    return d


def generarDic(v, n):
    count = 1
    d = {}
    for x in range(1,n+1):
        for y in range(1,n+1):
            d[v[count]] = { "row": x, "col": y}
            count += 1
    return d 


def iniciar_busqueda_con_a(vector, tam, estrategia):
    explorado = []
    prioridad = PriorityQueue()
    matriz_inicial = generarDic(vector,tam)
    matriz_objetivo = generarMeta(tam)
    raiz = Nodo(matriz_inicial, None, 0, None)
    raiz.metodo_a_utilizar(estrategia, matriz_objetivo)
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
                counter = nodo.expandir(prioridad, tam, matriz_objetivo, counter, estrategia) 
    print("Cantidad de Nodos visitados:",len((explorado)))


start = datetime.now()
end = datetime.now() - start
print("Tiempo de solucion: ", end)