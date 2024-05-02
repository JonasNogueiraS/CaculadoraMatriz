from modelo.matriz import Matriz
import numpy as np
from random import randint
from fractions import Fraction
class Matriz_controle:
    def __init__(self) -> None:
        self.__erro = ""

    def montar_matriz_interface(self, matriz: str) -> Matriz:
        M = []
        linhas = matriz.splitlines()
        for linha in linhas:
            valores = linha.split()
            nova_linha = []
            for valor in valores:
            # Converta o valor para fração
                nova_linha.append(Fraction(valor))
            M.append(nova_linha)
        new_matriz = Matriz(n=len(M), m=len(M[0]))
        new_matriz.valores = M
        return new_matriz
    
    def verificar_matriz_preenchida(self, matriz: Matriz) -> bool:
        
        for i in range(matriz.linha):
            for j in range(matriz.coluna):
                if matriz.valores[i][j] is None:
                    return False
        return True
            
    def matriz_transposta(self, B: Matriz) -> Matriz:
        matriz_t = Matriz(m=B.linha, n=B.coluna)  
        for i in range(B.linha):  
            for j in range(B.coluna):  
                matriz_t.valores[j][i] = B.valores[i][j]  
        
        return matriz_t
    
    def somar_matrizes(self, A: Matriz, B: Matriz) -> Matriz:
        if not self.verificar_matriz_preenchida(A) or not self.verificar_matriz_preenchida(B):
            self.erro = "Uma ou ambas as matrizes não estão preenchidas."
            return None
        
        if A.linha == B.linha and A.coluna == B.coluna:
            resultado = Matriz(n = A.linha, m = A.coluna)
            for i in range(A.linha):
                for j in range(A.coluna):
                    resultado.valores[i][j] = A.valores[i][j]+B.valores[i][j]
            
            return resultado
        else:
            self.erro = "Matrizes de ordem diferentes."
            return None
    
    def subtrair_matrizes(self, A: Matriz, B: Matriz) -> Matriz:
        if not self.verificar_matriz_preenchida(A) or not self.verificar_matriz_preenchida(B):
            self.erro = "Uma ou ambas as matrizes não estão preenchidas."
            return None
        
        if A.linha == B.linha and A.coluna == B.coluna:
            resultado = Matriz(n = A.linha, m = A.coluna)
            for i in range(A.linha):
                for j in range(A.coluna):
                    resultado.valores[i][j] = A.valores[i][j]-B.valores[i][j]
            
            return resultado
        else:
            self.erro = "Matrizes de ordem diferentes."
            return None
    
    def multiplicar_matrizes(self, A: Matriz, B: Matriz) -> Matriz:
        if not self.verificar_matriz_preenchida(A) or not self.verificar_matriz_preenchida(B):
            self.erro = "Uma ou ambas as matrizes não estão preenchidas."
            return None
        
        if A.coluna != B.linha:
            self.erro = "Numero de colunas da 1º Matriz é diferente do numero de linhas da 2º."
            return None
        
        resultado = Matriz(n=A.linha, m=B.coluna)
        for i in range(A.linha):
            for j in range(B.coluna):
                resultado.valores[i][j] = sum(A.valores[i][k]*B.valores[k][j] for k in range(A.coluna))
        return resultado
        
    def determinante_calc(self, B: Matriz) ->float:
        if not self.verificar_matriz_preenchida(B):
            self.erro = "A matriz não está preenchida."
            return None
    
        if B.linha != B.coluna:
            self.erro = "A matriz não é quadrada."
            return None
        
        b_np = np.array(B.valores)
        det = np.linalg.det(b_np)
        return det
    
    def gerar_matriz_magica(self, ordem: int) -> Matriz:
        if ordem % 2 == 1:
            return self.matriz_magica_impar(ordem)
        else:
            return self.matriz_magica_par(ordem)
    
    def matriz_magica_impar(self, ordem: int) -> Matriz:
        matriz_magica = [[0]*ordem for _ in range (ordem)]
        num = randint(1, 20)
        i, j = 0, ordem // 2
        n = num-1
        while num <= (ordem ** 2)+n:
            matriz_magica[i][j] = num
            num += 1
            novo_i, novo_j = (i-1)% ordem, (j+1)% ordem
            if matriz_magica[novo_i][novo_j]:
                i += 1
            else:
                i, j = novo_i, novo_j
        
        nova_matriz = Matriz(n=ordem, m=ordem)
        nova_matriz.valores = matriz_magica
        return nova_matriz
    
    def matriz_magica_par(self, ordem: int) -> Matriz:
        magic_square = [[0] * ordem for _ in range(ordem)]
        num = randint(1,20)  # Começa a partir de 1
        i, j = 0, ordem // 2
        n = num-1

    # Preenche a matriz de 1 a ordem**2
        while num <= (ordem**2)+n:
            magic_square[i][j] = num
            num += 1

            newi = (i - 1) % ordem
            newj = (j + 1) % ordem

        # Se a posição estiver ocupada, move uma linha para baixo
            if magic_square[newi][newj] != 0:
                i = (i + 1) % ordem
            else:
                i, j = newi, newj

    # Criação da matriz
        new_matriz = Matriz(n=ordem, m=ordem)
        new_matriz.valores = magic_square
        return new_matriz

    def calcular_inv(self, X: Matriz) -> Matriz:
        if not self.verificar_matriz_preenchida(X):
            self.erro = "A matriz não está preenchida."
            return None

        if X.linha != X.coluna:
            self.erro = "A matriz não é quadrada."
            return None
        
        if self.determinante_calc(X) == 0:
            self.erro = "A matriz é singular, não possui inversa."
            return None
        
        matriz_np = np.array(X.valores)
        matriz_inversa_np = np.linalg.inv(matriz_np)
        
        matriz_inversa = Matriz(n=X.linha, m=X.coluna)
        matriz_inversa.valores = matriz_inversa_np.tolist()
        
        return matriz_inversa
    