import eel
import time
from .estado import Nodo
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
    count = 0
    d = {}
    for x in range(1,n+1):
        for y in range(1,n+1):
            d[v[count]] = { "row": x, "col": y}
            count += 1
    return d 

@eel.expose
def iniciar_busqueda_con_a(vector, tam, estrategia):
    s = None
    explorado = []
    prioridad = PriorityQueue()
    matriz_inicial = generarDic(vector, tam)
    matriz_objetivo = generarMeta(tam)
    raiz = Nodo(matriz_inicial, None, 0, None)
    t_ini = time.time()
    raiz.metodo_a_utilizar(estrategia, matriz_objetivo)
    counter = 0
    prioridad.put((raiz.costo_f, counter, raiz))
    while not prioridad.empty():
        item = prioridad.get()
        nodo = item[2]

        if (time.time() - t_ini) * 1000 > 300000:
            print("Busqueda A* no pudo encontrar una solucion pasados 5 minutos.")
            return False
        
        if nodo.matriz == matriz_objetivo:
            s = nodo.solucion()
            nodo_fin = nodo
            print("Camino de la solucion:", s)
            break          
        else:
            if nodo.matriz not in explorado:
                explorado.append(nodo.matriz)
                counter = nodo.expandir(prioridad, tam, matriz_objetivo, counter, estrategia)
    t_fin = time.time()
    t_total = t_fin - t_ini
    mat_fin = [i for i in range(1, tam ** 2)]
    mat_fin.append('')
    return {
        'tiempo': round(t_total*1000),   # en milisegundos
        'cant_nodos': len(explorado),
        'matriz_fin': mat_fin,
        'solucion': s
    }