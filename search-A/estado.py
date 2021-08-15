
class Nodo:

    def __init__(self, matriz, nodo_padre, costo, direccion):
        self.matriz =  matriz
        self.nodo_padre = nodo_padre
        self.direccion = direccion
        self.costo_g = costo
        self.heuristica = 0
        self.costo_f = 0 


    def distancia_manhattan(self, matriz_meta):
        for key in matriz_meta.keys():
            if key != "":
                m1 = abs(self.matriz[key]["row"] - matriz_meta[key]["row"])
                m2 = abs(self.matriz[key]["col"] - matriz_meta[key]["col"])
                self.heuristica += m1 + m2 
        self.costo_f = self.costo_g + self.heuristica 


    def mal_posicionados(self, matriz_meta):
    	for key in matriz_meta.keys():
    		if key != "" and (self.matriz[key]["row"] != matriz_meta[key]["row"] or self.matriz[key]["col"] != matriz_meta[key]["col"]):
    				self.heuristica += 1
    	self.costo_f= self.heuristica + self.costo_g
    
    
    def solucion(self):
        print("Encontro solucion")
        pasos_solucion = []
        pasos_solucion.append(self.direccion)
        nodo = self
        while nodo.nodo_padre != None:
            nodo = nodo.nodo_padre
            pasos_solucion.append(nodo.direccion)
        pasos_solucion = pasos_solucion[:-1]
        return pasos_solucion[::-1] 

    
    def expandir(self, queuePriority, size, m_meta, counter):
        vacio = self.matriz[""]
        derecha = { "row": vacio["row"], "col": vacio["col"] + 1} if vacio["col"] +  1 <= size else None
        izquierda = { "row": vacio["row"], "col": vacio["col"] - 1} if vacio["col"] -  1 > 0 else None
        arriba = { "row": vacio["row"] - 1, "col": vacio["col"]} if vacio["row"] -  1 > 0 else None
        abajo = { "row": vacio["row"] + 1, "col": vacio["col"]} if vacio["row"] +  1 <= size else None 
        for key in self.matriz.keys():
            if key != "":
                if arriba is not None and self.matriz[key]["row"] == arriba["row"] and self.matriz[key]["col"] == arriba["col"]:
                    counter += 1
                    queuePriority.put(self.moverPieza(key, arriba, "arriba", m_meta, counter))
                elif derecha is not None and self.matriz[key]["row"] == derecha["row"] and self.matriz[key]["col"] == derecha["col"]:
                    counter += 1
                    queuePriority.put(self.moverPieza(key, derecha, "derecha", m_meta, counter))
                elif abajo is not None and self.matriz[key]["row"] == abajo["row"] and self.matriz[key]["col"] == abajo["col"]:
                    counter += 1
                    queuePriority.put(self.moverPieza(key, abajo, "abajo", m_meta, counter))
                elif izquierda is not None and self.matriz[key]["row"] == izquierda["row"] and self.matriz[key]["col"] == izquierda["col"]:
                    counter += 1
                    queuePriority.put(self.moverPieza(key, izquierda, "izquierda", m_meta, counter)) 
        return counter

    
    def moverPieza(self, key_pieza, pos_next, name, m_meta1, counter):
        temp_matriz = self.matriz.copy()
        temp_matriz[key_pieza] = temp_matriz[""]
        temp_matriz[""] = pos_next
        new_nodo = Nodo(temp_matriz, self, self.costo_g + 1, name)
        new_nodo.distancia_manhattan(m_meta1)
        return (new_nodo.costo_f, counter, new_nodo)
