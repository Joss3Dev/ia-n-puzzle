class Estado:

    def __init__(self, matriz):
        self.matriz = matriz
        self.pos_vacio = 0
        self.padre = 0
        self.altura = 0

    def bfs(self, estado_inicial):
        """
        * Primero encolar el primer estado
        * Despues entrar a un loop que desencole cada estado y al desencolar procesar que nuevos movimientos puede
        tomar ese estado
        * Verifica si no es un estado final
        *
        :param estado_inicial:
        :return:
        """
        cola = []
        cola.append(estado_inicial)
        while len(cola) > 0:
            estado_actual = cola.pop()
            # VERIFICA SI ES QUE ES UN ESTADO FINAL O NO
            estados_siguientes = estado_actual.evaluar_movimientos()
            cola.append(estados_siguientes)

    def evaluar_movimientos(self):
        """
        Tiene que recibir un objeto Estado, con el debe evaluar que movimientos se pueden hacer tomando en cuenta donde
        esta la casilla vacia, la cantidad de columnas que tiene el puzle y retornar todos lo movimientos que se pueden
        hacer

        En un puzle unidimencional:
        movimiento izquierda: indice - 1
        movimiento derecha: indice + 1
        movimiento arriba: indice - cantidad_columnas
        movimiento abajo: indice + cantidad_columnas

        Si esta en la frontera derecha, osea, (indice + 1) % cantidad_columnas == 0, entonces no puede moverse a la derecha
        Si esta en la frontera izquieda, osea, indice % cantidad_columnas == 0, entonces mo puede moverse a la izquierda
        Si esta en la frontera superior, osea, 0 <= indice <= cantidad_columnas - 1, entonces no puede moverse hacia arriba
        Si esta en la frontera inferior, osea, N - cantidad_columnas + 1 <= indice <= N, entonces no puede moverse hacia abajo
        """


