from math import sqrt
import random
from estado import Nodo

N = int(input("N-Puzzle: "))
tam = int(sqrt(N + 1))

#Estado Objetivo
matriz_objetivo = {}
valor = 1
for x in range(1,tam+1):
    for y in range(1,tam+1):
        if x == 1 and y == 1:
            matriz_objetivo[""] = { "row": 1, "col": 1}
        else:
            matriz_objetivo[valor] = { "row": x, "col": y}
            valor += 1


matriz_inicial = {}
valores = list(range(1,N+1)) + [""] 
rand = random.sample(valores, N+1)
count = 0
for x in range(1,tam+1):
    for y in range(1,tam+1):
        matriz_inicial[rand[count]] = { "row": x, "col": y}
        count += 1


def init_search():
    repetido = []
    nodo = Nodo(matriz_inicial, 0)
    nodo.distancia_manhattan(matriz_objetivo)
    pila = [nodo]
    while len(pila) > 0:
        estado = pila.pop()
        if comparar(estado.puzzle, matriz_objetivo) == True:
            break
        else:
            if verificarEstadoRepetido(repetido,estado.puzzle) != True:
                repetido.append(estado.puzzle)
                pila = pila + expandir(estado)
    return len(repetido)+1


def expandir(estado):
    sucesores = [] 
    celda = estado.puzzle[""]
    derecha = { "row": celda["row"], "col": celda["col"] + 1} if celda["col"] +  1 <= tam else None
    izquierda = { "row": celda["row"], "col": celda["col"] - 1} if celda["col"] -  1 > 0 else None
    arriba = { "row": celda["row"] - 1, "col": celda["col"]} if celda["row"] -  1 > 0 else None
    abajo = { "row": celda["row"] + 1, "col": celda["col"]} if celda["row"] +  1 <= tam else None 
    m_actual = estado.puzzle.copy()
    del m_actual[""]
    for key in m_actual.keys():
        if arriba is not None and m_actual[key]["row"] == arriba["row"] and m_actual[key]["col"] == arriba["col"]:
            nueva_m = m_actual.copy()
            nueva_m[""] = arriba
            nueva_m[key] = celda 
            nuevo_nodo = Nodo(nueva_m, estado.coste_nodo + 1)
            nuevo_nodo.distancia_manhattan(matriz_objetivo)
            sucesores.append(nuevo_nodo)
        elif derecha is not None and m_actual[key]["row"] == derecha["row"] and m_actual[key]["col"] == derecha["col"]:
            nueva_m = m_actual.copy()
            nueva_m[""] = derecha
            nueva_m[key] = celda 
            nuevo_nodo = Nodo(nueva_m, estado.coste_nodo + 1)
            nuevo_nodo.distancia_manhattan(matriz_objetivo) 
            sucesores.append(nuevo_nodo)
        elif abajo is not None and m_actual[key]["row"] == abajo["row"] and m_actual[key]["col"] == abajo["col"]:
            nueva_m = m_actual.copy()
            nueva_m[""] = abajo
            nueva_m[key] = celda 
            nuevo_nodo = Nodo(nueva_m, estado.coste_nodo + 1)
            nuevo_nodo.distancia_manhattan(matriz_objetivo)
            sucesores.append(nuevo_nodo)
        elif izquierda is not None and m_actual[key]["row"] == izquierda["row"] and m_actual[key]["col"] == izquierda["col"]:
            nueva_m = m_actual.copy()
            nueva_m[""] = izquierda
            nueva_m[key] = celda 
            nuevo_nodo = Nodo(nueva_m, estado.coste_nodo + 1)
            nuevo_nodo.distancia_manhattan(matriz_objetivo)
            sucesores.append(nuevo_nodo)
    sucesores.sort(key=order, reverse=True)
    return sucesores

def order(n):
    return n.total

def verificarEstadoRepetido(lista, matriz):
    ban = False 
    for m in lista:
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

#print(matriz_inicial)
print("Cantidad de Nodos visitados:",init_search())