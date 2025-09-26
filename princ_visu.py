import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from Nova_inter import Ui_MainWindow
from controle.matriz_control import Matriz_controle


class Visu_princ(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Calculcadora de Matrizes")
        self.iniciar_componentes()
        self.matriz_controle = Matriz_controle ()
        self.label.setPixmap(QPixmap('visao/imagens/quadro-PNG.png'))
        self.label_Emoji.setPixmap(QPixmap('visao/imagens/emoji.png'))
        self.label_chao931x31.setPixmap(QPixmap('visao/imagens/chao_madeira.png'))
        self.label_Balao211x51.setPixmap(QPixmap('visao/imagens/balao-removebg-preview.png'))
        self.label_AvISO61x51.setPixmap(QPixmap('visao/imagens/anota.png'))
        
    def iniciar_componentes(self):
        self.pushButton_TRANSPOSTA_A.clicked.connect(self.mostrar_transposta_A)
        self.pushButton_TRANSPOSTA_B.clicked.connect(self.mostrar_transposta_B)
        self.pushButton_SOMA.clicked.connect(self.somar_matriz)
        self.pushButton_SUBTRAIR.clicked.connect(self.sub_matriz)
        self.pushButton_MULTIPLICAR.clicked.connect(self.multi_matrizes)
        self.pushButton_DET_A.clicked.connect(self.calcular_det_A)
        self.pushButton_DETERMINANTE_B.clicked.connect(self.calcular_det_B)
        self.pushButton_GERAR_MAGICA.clicked.connect(self.Matriz_magica)
        self.pushButton_INV_A.clicked.connect(self.calcular_inversa_A)
        self.pushButton_INV_B.clicked.connect(self.calcular_inversa_B)
          
    def imprimir_resultados(self, texto):
        self.textEdit_RESULTADO.setText("")
        self.textEdit_RESULTADO.setText(f'{texto}')
    
    def imprimir_msg_usuario(self, texto):
        self.label_MSGUSUARIO.setText(texto)
    
    def verificar_texto_vazio(self, texto, mensagem_aviso):
        if not texto.strip():  # Verifica se o texto está vazio ou contém apenas espaços em branco
            self.imprimir_msg_usuario(mensagem_aviso)
            return True
        return False

    def somar_matriz(self):
        matriz_A_string = self.textEdit_MATRIZ_A.toPlainText()
        matriz_B_string = self.textEdit_MATRIZ_B.toPlainText()

        if self.verificar_texto_vazio(matriz_A_string, "Por favor, preencha a Matriz A."):
            return
        if self.verificar_texto_vazio(matriz_B_string, "Por favor, preencha a Matriz B."):
            return

        matriz_A_int = self.matriz_controle.montar_matriz_interface(matriz_A_string)
        matriz_B_int = self.matriz_controle.montar_matriz_interface(matriz_B_string)
        
        if matriz_A_int is None:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")  
            return

        if matriz_B_int is None:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")  
            return

        resultado = self.matriz_controle.somar_matrizes(matriz_A_int, matriz_B_int)

        if resultado is not None:
            self.imprimir_resultados(resultado.valores)
            self.imprimir_msg_usuario("Soma realizada com sucesso.")
        else:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")  

    def sub_matriz(self):
        matriz_A_string = self.textEdit_MATRIZ_A.toPlainText()
        matriz_B_string = self.textEdit_MATRIZ_B.toPlainText()

        if self.verificar_texto_vazio(matriz_A_string, "Por favor, preencha a Matriz A."):
            return
        if self.verificar_texto_vazio(matriz_B_string, "Por favor, preencha a Matriz B."):
            return

        matriz_A_int = self.matriz_controle.montar_matriz_interface(matriz_A_string)
        matriz_B_int = self.matriz_controle.montar_matriz_interface(matriz_B_string)

        resultado = self.matriz_controle.subtrair_matrizes(matriz_A_int, matriz_B_int)

        if resultado is not None:
            self.imprimir_resultados(resultado.valores)
            self.imprimir_msg_usuario("Subtração realizada com sucesso.")
        else:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("") 

    def mostrar_transposta_A(self):
        matriz_interf_A_texto = self.textEdit_MATRIZ_A.toPlainText()

        if self.verificar_texto_vazio(matriz_interf_A_texto, "Por favor, preencha a Matriz A."):
            return

        matriz_temporaria_int = self.matriz_controle.montar_matriz_interface(matriz_interf_A_texto)
        matriz_transpost = self.matriz_controle.matriz_transposta(matriz_temporaria_int)
        self.imprimir_resultados(matriz_transpost.valores)
        self.imprimir_msg_usuario("Matriz tranposta de A gerada.")

    def mostrar_transposta_B(self):
        matriz_interf_B_texto = self.textEdit_MATRIZ_B.toPlainText()

        if self.verificar_texto_vazio(matriz_interf_B_texto, "Preencha a Matriz B."):
            return

        matriz_temporaria_int = self.matriz_controle.montar_matriz_interface(matriz_interf_B_texto)
        matriz_transpost = self.matriz_controle.matriz_transposta(matriz_temporaria_int)
        self.imprimir_resultados(matriz_transpost.valores)
        self.imprimir_msg_usuario("Transposta de B gerada.")

    def multi_matrizes(self):
        matriz_A_string = self.textEdit_MATRIZ_A.toPlainText()
        matriz_B_string = self.textEdit_MATRIZ_B.toPlainText()

        if self.verificar_texto_vazio(matriz_A_string, "Por favor, preencha a Matriz A."):
            return
        if self.verificar_texto_vazio(matriz_B_string, "Por favor, preencha a Matriz B."):
            return

        matriz_A_int = self.matriz_controle.montar_matriz_interface(matriz_A_string)
        matriz_B_int = self.matriz_controle.montar_matriz_interface(matriz_B_string)

        resultado = self.matriz_controle.multiplicar_matrizes(matriz_A_int, matriz_B_int)

        if resultado is not None:
            self.imprimir_resultados(resultado.valores)
            self.imprimir_msg_usuario("Multiplicação realizada com sucesso.")
        else:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")  # Limpa a área de resultados

    def calcular_det_A(self):
        matriz_interf_A_texto = self.textEdit_MATRIZ_A.toPlainText()

        if self.verificar_texto_vazio(matriz_interf_A_texto, "Por favor, preencha a Matriz A."):
            return

        matriz_temporaria_int = self.matriz_controle.montar_matriz_interface(matriz_interf_A_texto)
        determinante_A = self.matriz_controle.determinante_calc(matriz_temporaria_int)

        if determinante_A is not None:
            self.imprimir_resultados(determinante_A)
            self.imprimir_msg_usuario("Determinante calculado com sucesso.")
        else:
            self.erro = self.matriz_controle.erro
            self.imprimir_resultados("")
            self.imprimir_msg_usuario(self.erro)

    def calcular_det_B(self):
        matriz_interf_B_texto = self.textEdit_MATRIZ_B.toPlainText()

        if self.verificar_texto_vazio(matriz_interf_B_texto, "Por favor, preencha a Matriz B."):
            return

        matriz_temporaria_int = self.matriz_controle.montar_matriz_interface(matriz_interf_B_texto)
        determinante_B = self.matriz_controle.determinante_calc(matriz_temporaria_int)

        if determinante_B is not None:
            self.imprimir_resultados(determinante_B)
            self.imprimir_msg_usuario("Determinante calculado com sucesso.")
        else:
            self.erro = self.matriz_controle.erro
            self.imprimir_resultados("")
            self.imprimir_msg_usuario(self.erro)
    
    def Matriz_magica(self):
        ordem_magica_text = self.lineEdit_ORDEM_MAGICA.text()
        
        if self.verificar_texto_vazio(ordem_magica_text, "Por favor, digite a ordem da matriz."):
            return

        ordem_magica = int(ordem_magica_text)
        
        matriz_magica = self.matriz_controle.gerar_matriz_magica(ordem_magica)
        
        self.imprimir_resultados(matriz_magica.valores)
        self.imprimir_msg_usuario("Matriz magica gerada com sucesso!")
    
    def calcular_inversa_A(self):
        matriz_interf_texto = self.textEdit_MATRIZ_A.toPlainText()

        if self.verificar_texto_vazio(matriz_interf_texto, "Por favor, preencha a matriz."):
            return

        matriz_int = self.matriz_controle.montar_matriz_interface(matriz_interf_texto)
        
        if matriz_int is None:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")  
            return

        matriz_inversa = self.matriz_controle.calcular_inv(matriz_int)

        if matriz_inversa is not None:
            self.imprimir_resultados(matriz_inversa.valores)
            self.imprimir_msg_usuario("Matriz inversa calculada com sucesso.")
        else:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")
    
    def calcular_inversa_B(self):
        matriz_interf_texto = self.textEdit_MATRIZ_B.toPlainText()

        if self.verificar_texto_vazio(matriz_interf_texto, "Por favor, preencha a matriz."):
            return

        matriz_int = self.matriz_controle.montar_matriz_interface(matriz_interf_texto)
        
        if matriz_int is None:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")  
            return

        matriz_inversa = self.matriz_controle.calcular_inv(matriz_int)

        if matriz_inversa is not None:
            self.imprimir_resultados(matriz_inversa.valores)
            self.imprimir_msg_usuario("Matriz inversa calculada com sucesso.")
        else:
            self.imprimir_msg_usuario(self.matriz_controle.erro)
            self.imprimir_resultados("")
    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    visao = Visu_princ()
    visao.show()
    qt.exec()