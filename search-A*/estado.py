
class Nodo:

    def __init__(self, puzzle,G):
        self.puzzle = puzzle
        self.coste_nodo = G
        self.coste_objetivo = 0

    def distancia_manhattan(self, matrizObjetivo):
        m_copy = matrizObjetivo.copy()
        del m_copy[""]
        for key in m_copy.keys():
            m1 = self.puzzle[key]["row"] + self.puzzle[key]["col"]
            m2 = m_copy[key]["row"] + m_copy[key]["col"]
            self.coste_objetivo += abs(m1-m2)
        self.total = self.coste_nodo = self.coste_objetivo 
    
