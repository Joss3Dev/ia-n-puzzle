import math, time


class Estado:

    def __init__(self, matriz, pos_vacio, padre, altura):
        self.matriz = matriz
        self.pos_vacio = pos_vacio
        self.padre = padre
        self.altura = altura

    def bfs(self):
        cola = []
        cola.append(self)
        nodos_expandidos = 0
        estados_explorados = []
        final = None
        t_ini = time.time()
        while len(cola) > 0 and not final:
            if (time.time() - t_ini) * 1000 > 30000:
                print("BFS no pudo encontrar una solucion pasados 30 segundos")
                break
            nodos_expandidos += 1
            estado_actual = cola.pop(0)
            if estado_actual.es_estado_final():
                final = estado_actual
            elif estado_actual.matriz not in estados_explorados:
                estados_siguientes = estado_actual.evaluar_movimientos()
                estados_explorados.append(estado_actual.matriz)
                cola.extend(estados_siguientes)
        t_fin = time.time()
        t_total = t_fin - t_ini
        return t_total, nodos_expandidos, self.matriz, final.matriz

    def evaluar_movimientos(self):
        """
        Tiene que recibir un objeto Estado, con el debe evaluar que movimientos se pueden hacer tomando en cuenta donde
        esta la casilla vacia, la cantidad de columnas que tiene el puzzle y retornar todos lo movimientos que se pueden
        hacer

        En un puzzle unidimensional:
        movimiento izquierda: indice - 1
        movimiento derecha: indice + 1
        movimiento arriba: indice - cantidad_columnas
        movimiento abajo: indice + cantidad_columnas

        Si esta en la frontera derecha, osea, (indice + 1) % cantidad_columnas == 0, entonces no puede moverse a la derecha
        Si esta en la frontera izquieda, osea, indice % cantidad_columnas == 0, entonces mo puede moverse a la izquierda
        Si esta en la frontera superior, osea, 0 <= indice <= cantidad_columnas - 1, entonces no puede moverse hacia arriba
        Si esta en la frontera inferior, osea, N - cantidad_columnas + 1 <= indice <= N, entonces no puede moverse hacia abajo
        """
        nuevos_estados = []
        cant_cols = math.sqrt(len(self.matriz))
        if not (self.pos_vacio + 1) % cant_cols == 0:
            nuevo_estado = self.mover('der')
            nuevos_estados.append(nuevo_estado)
        if not self.pos_vacio % cant_cols == 0:
            nuevo_estado = self.mover('izq')
            nuevos_estados.append(nuevo_estado)
        if not 0 <= self.pos_vacio <= cant_cols - 1:
            nuevo_estado = self.mover('arr')
            nuevos_estados.append(nuevo_estado)
        if not (cant_cols ** 2 - cant_cols) <= self.pos_vacio < len(self.matriz):
            nuevo_estado = self.mover('abj')
            nuevos_estados.append(nuevo_estado)
        return nuevos_estados

    def mover(self, dir):
        matriz = self.matriz.copy()
        indice = self.pos_vacio
        if dir == 'der':
            matriz[indice], matriz[indice+1] = matriz[indice+1], matriz[indice]
            indice = indice + 1
        elif dir == 'izq':
            matriz[indice], matriz[indice-1] = matriz[indice-1], matriz[indice]
            indice = indice - 1
        elif dir == 'arr':
            cant_cols = int(math.sqrt(len(self.matriz)))
            matriz[indice], matriz[indice - cant_cols] = matriz[indice - cant_cols], matriz[indice]
            indice = indice - cant_cols
        elif dir == 'abj':
            cant_cols = int(math.sqrt(len(self.matriz)))
            matriz[indice], matriz[indice + cant_cols] = matriz[indice + cant_cols], matriz[indice]
            indice = indice + cant_cols
        nuevo_estado = Estado(matriz, indice, self, self.altura + 1)
        return nuevo_estado

    def es_estado_final(self):
        matriz = self.matriz
        for i in range(len(matriz)-1):
            if matriz[i] > matriz[i + 1]:
                return False
        return True