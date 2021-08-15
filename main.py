import eel 
import random

eel.init("gui")  

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
        solucionable =  True if count % 2 == 0 else False
    return rand 


eel.start("vista.html", mode="default")
