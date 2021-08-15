import math, time
import eel


class Estado:

    def __init__(self, matriz, pos_vacio, padre, altura, dir):
        self.matriz = matriz
        self.pos_vacio = pos_vacio
        self.padre = padre
        self.altura = altura
        self.dir_padre = dir

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
                return (time.time() - t_ini) * 1000, nodos_expandidos, self.matriz, False, False
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
        if final:
            return t_total, nodos_expandidos, self.matriz, final.matriz, final.get_cadena_solucion()
        else:
            return t_total, nodos_expandidos, self.matriz, None, None

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
        nuevo_estado = Estado(matriz, indice, self, self.altura + 1, dir)
        return nuevo_estado

    def es_estado_final(self):
        matriz = self.matriz
        for i in range(len(matriz)-1):
            if matriz[i] > matriz[i + 1]:
                return False
        return True

    def solucion(self):
        soluc = []
        if self.dir_padre:
            soluc.extend(self.padre.solucion())
            if self.dir_padre == 'der':
                soluc.append('Derecha')
            elif self.dir_padre == 'izq':
                soluc.append('Izquierda')
            elif self.dir_padre == 'arr':
                soluc.append('Arriba')
            elif self.dir_padre == 'abj':
                soluc.append('Abajo')
            return soluc
        else:
            return []

    def get_cadena_solucion(self):
        list_mov = self.solucion()
        camino = ''
        for dir in list_mov:
            camino = camino + dir + ','
        return camino[:-1]

@eel.expose
def iniciar_bfs(matriz, n):
    pos_vacio = matriz.index('')
    matriz[pos_vacio] = int(n)*100
    nuevo_estado = Estado(matriz, pos_vacio, None, 0, None)
    tiempo, cant_nodos, matriz_ini, matriz_fin, camino_sol = nuevo_estado.bfs()
    if matriz_fin:
        matriz_ini[matriz_ini.index(int(n)*100)] = ''
        matriz_fin[matriz_fin.index(int(n)*100)] = ''
        return {
            'tiempo': round(tiempo*1000),   # en milisegundos
            'cant_nodos': cant_nodos,
            'matriz_fin': matriz_fin,
            'solucion': camino_sol
        }
    else:
        return False