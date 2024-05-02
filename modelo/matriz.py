import numpy as np

class Matriz:
    def __init__(self, n=None, m=None) -> None:
        self.linha = n
        self.coluna = m
        self.valores = self.criar_matriz_nula()
    
    @property
    def valores(self):
        return self.__valores

    @valores.setter
    def valores(self, valores):
        M_int = self.criar_matriz_nula()
        for i in range(0, len(M_int)):
            for j in range(0, len(M_int[0])):
                M_int[i][j] = float(valores[i][j])
        self.__valores = M_int
    
    @property
    def coluna(self):
        return self.__coluna
    
    @coluna.setter
    def coluna(self, coluna):
        if coluna <= 0:
            print("Erro")
        else:
            self.__coluna = coluna
    
    @property
    def linha(self):
        return self.__linha
    
    @linha.setter
    def linha(self, n):
        if n <= 0:
            print("Erro")
        else:
            self.__linha = n
    
    def criar_matriz_nula(self):
        return np.zeros((self.linha, self.coluna))
