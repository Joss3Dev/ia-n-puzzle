import eel 
import random
from bfs.Estado import iniciar_bfs
from search_a.search import iniciar_busqueda_con_a

eel.init("C:/Users/Jose/Documents/ia-n-puzzle/gui")

rand = None
N = None

@eel.expose
def generarEstadoInicial(size):
    N = int(size)
    valores = list(range(1,N*N)) + [""]
    solucionable = False
    while not solucionable: 
        rand =  random.sample(valores, N*N)
        count = 0
        for i in range(0,len(rand)-1):
            for j in range(i+1, len(rand)):
                if (rand[i] != "" and rand[j] != "" and rand[i] > rand[j]):
                    count += 1
        solucionable = True if count % 2 == 0 else False
    return rand

@eel.expose
def llamar_bfs(matriz, n):
    return iniciar_bfs(matriz, n)

@eel.expose
def llamar_manhattan(matriz, n):
    return iniciar_busqueda_con_a(matriz, n, True)

@eel.expose
def llamar_piezas_incorrectas(matriz, n):
    return iniciar_busqueda_con_a(matriz, n, False)


eel.start("vista.html", mode="default")
