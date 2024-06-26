# Form implementation generated from reading ui file 'interfaceCalcMatriz.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 528)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_fundo = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_fundo.setGeometry(QtCore.QRect(0, 0, 637, 533))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame_fundo.setFont(font)
        self.frame_fundo.setStyleSheet("background-color: rgb(211, 248, 255);")
        self.frame_fundo.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_fundo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fundo.setObjectName("frame_fundo")
        self.label_Titulo = QtWidgets.QLabel(parent=self.frame_fundo)
        self.label_Titulo.setGeometry(QtCore.QRect(200, 20, 251, 41))
        self.label_Titulo.setObjectName("label_Titulo")
        self.frame_2msg = QtWidgets.QFrame(parent=self.frame_fundo)
        self.frame_2msg.setGeometry(QtCore.QRect(110, 60, 421, 43))
        self.frame_2msg.setStyleSheet("background-color: rgb(234, 254, 255);")
        self.frame_2msg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2msg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2msg.setObjectName("frame_2msg")
        self.label_mensagem = QtWidgets.QLabel(parent=self.frame_2msg)
        self.label_mensagem.setGeometry(QtCore.QRect(10, 10, 401, 21))
        self.label_mensagem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_mensagem.setObjectName("label_mensagem")
        self.frame_Opcoes = QtWidgets.QFrame(parent=self.frame_fundo)
        self.frame_Opcoes.setGeometry(QtCore.QRect(9, 119, 619, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame_Opcoes.setFont(font)
        self.frame_Opcoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Opcoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Opcoes.setObjectName("frame_Opcoes")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_Opcoes)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_MULT = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_MULT.setFont(font)
        self.pushButton_MULT.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_MULT.setObjectName("pushButton_MULT")
        self.gridLayout.addWidget(self.pushButton_MULT, 3, 1, 1, 1)
        self.pushButton_DET_A = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_DET_A.setFont(font)
        self.pushButton_DET_A.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_DET_A.setObjectName("pushButton_DET_A")
        self.gridLayout.addWidget(self.pushButton_DET_A, 6, 0, 1, 1)
        self.label_IdentificarMat_A = QtWidgets.QLabel(parent=self.frame_Opcoes)
        self.label_IdentificarMat_A.setObjectName("label_IdentificarMat_A")
        self.gridLayout.addWidget(self.label_IdentificarMat_A, 0, 0, 1, 1)
        self.pushButton_TRANSPOSTA_B = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_TRANSPOSTA_B.setFont(font)
        self.pushButton_TRANSPOSTA_B.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_TRANSPOSTA_B.setObjectName("pushButton_TRANSPOSTA_B")
        self.gridLayout.addWidget(self.pushButton_TRANSPOSTA_B, 5, 2, 1, 1)
        self.pushButton_TRANSPOSTA_A = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_TRANSPOSTA_A.setFont(font)
        self.pushButton_TRANSPOSTA_A.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_TRANSPOSTA_A.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_TRANSPOSTA_A.setObjectName("pushButton_TRANSPOSTA_A")
        self.gridLayout.addWidget(self.pushButton_TRANSPOSTA_A, 5, 0, 1, 1)
        self.pushButton_SOMA = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SOMA.sizePolicy().hasHeightForWidth())
        self.pushButton_SOMA.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SOMA.setFont(font)
        self.pushButton_SOMA.setStyleSheet("\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.142, y1:0.0227273, x2:1, y2:0, stop:0 rgba(0, 50, 66, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_SOMA.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_SOMA.setObjectName("pushButton_SOMA")
        self.gridLayout.addWidget(self.pushButton_SOMA, 1, 1, 1, 1)
        self.label_Identificar_Mat_B = QtWidgets.QLabel(parent=self.frame_Opcoes)
        self.label_Identificar_Mat_B.setObjectName("label_Identificar_Mat_B")
        self.gridLayout.addWidget(self.label_Identificar_Mat_B, 0, 2, 1, 1)
        self.pushButton_SUBTRACAO = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SUBTRACAO.setFont(font)
        self.pushButton_SUBTRACAO.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_SUBTRACAO.setObjectName("pushButton_SUBTRACAO")
        self.gridLayout.addWidget(self.pushButton_SUBTRACAO, 2, 1, 1, 1)
        self.pushButton_DET_B = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_DET_B.setFont(font)
        self.pushButton_DET_B.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_DET_B.setObjectName("pushButton_DET_B")
        self.gridLayout.addWidget(self.pushButton_DET_B, 6, 2, 1, 1)
        self.textEdit_MatrizB = QtWidgets.QTextEdit(parent=self.frame_Opcoes)
        self.textEdit_MatrizB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_MatrizB.setObjectName("textEdit_MatrizB")
        self.gridLayout.addWidget(self.textEdit_MatrizB, 1, 2, 4, 1)
        self.pushButton_Matriz_MAGICA = QtWidgets.QPushButton(parent=self.frame_Opcoes)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Matriz_MAGICA.setFont(font)
        self.pushButton_Matriz_MAGICA.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255, 221, 196);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"")
        self.pushButton_Matriz_MAGICA.setObjectName("pushButton_Matriz_MAGICA")
        self.gridLayout.addWidget(self.pushButton_Matriz_MAGICA, 4, 1, 1, 1)
        self.textEdit_MatrizA = QtWidgets.QTextEdit(parent=self.frame_Opcoes)
        self.textEdit_MatrizA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_MatrizA.setObjectName("textEdit_MatrizA")
        self.gridLayout.addWidget(self.textEdit_MatrizA, 1, 0, 4, 1)
        self.OrdemMAtrizMAgica = QtWidgets.QSpinBox(parent=self.frame_Opcoes)
        self.OrdemMAtrizMAgica.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OrdemMAtrizMAgica.setObjectName("OrdemMAtrizMAgica")
        self.gridLayout.addWidget(self.OrdemMAtrizMAgica, 5, 1, 1, 1)
        self.textEdit_RESULT_OP = QtWidgets.QTextEdit(parent=self.frame_fundo)
        self.textEdit_RESULT_OP.setGeometry(QtCore.QRect(70, 342, 511, 171))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_RESULT_OP.setFont(font)
        self.textEdit_RESULT_OP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_RESULT_OP.setObjectName("textEdit_RESULT_OP")
        self.label_Resultado = QtWidgets.QLabel(parent=self.frame_fundo)
        self.label_Resultado.setGeometry(QtCore.QRect(240, 316, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Resultado.setFont(font)
        self.label_Resultado.setObjectName("label_Resultado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Titulo.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_Titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CALCULADORA DE MATRIZES</span></p></body></html>"))
        self.label_mensagem.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_MULT.setText(_translate("MainWindow", "Multiplicar (x)"))
        self.pushButton_DET_A.setText(_translate("MainWindow", "Determinante de A"))
        self.label_IdentificarMat_A.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Matriz A:</span></p></body></html>"))
        self.pushButton_TRANSPOSTA_B.setText(_translate("MainWindow", "Tansposta Matriz B"))
        self.pushButton_TRANSPOSTA_A.setText(_translate("MainWindow", "Tansposta Matriz A"))
        self.pushButton_SOMA.setText(_translate("MainWindow", "Somar(+)"))
        self.label_Identificar_Mat_B.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Matriz B:</span></p></body></html>"))
        self.pushButton_SUBTRACAO.setText(_translate("MainWindow", "Subtrair(-)"))
        self.pushButton_DET_B.setText(_translate("MainWindow", "Determinante de B"))
        self.textEdit_MatrizB.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_Matriz_MAGICA.setText(_translate("MainWindow", "Matriz Mágica"))
        self.textEdit_MatrizA.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_RESULT_OP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_Resultado.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">RESULTADO</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
