from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget)
from qdarktheme import load_stylesheet

font = QFont()
font.setPixelSize(24)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        tela = QWidget()
        layout = QVBoxLayout()

        #Botões ///////////////////////////////-
        but1 = QPushButton('Oráculo')
        but1.clicked.connect(lambda: print('hello'))
        but2 = QPushButton('Enviar Resposta')
        but2.clicked.connect(lambda: print('hello'))
        #//////////////////////////////////////-


        #Texto ////////////////////////////////-
        self.texto = QLabel('The Huxley 2.0')
        self.texto.setFont(font)
        self.texto.setAlignment(Qt.AlignCenter)
        #//////////////////////////////////////-


        #Menu /////////////////////////////////-
        menu = self.menuBar()
        arquivo_menu = menu.addMenu('Menu')
        action = QAction('Print!', self)
        arquivo_menu.addAction(action)
        #//////////////////////////////////////-


        layout.addWidget(self.texto)
        layout.addWidget(but1)
        layout.addWidget(but2)


        tela.setLayout(layout)
        self.setCentralWidget(tela)
        
   
class OtherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        tela = QWidget()
        layout = QVBoxLayout()
        
        #Texto ////////////////////////////////-
        texto = QLabel('Hello World!')
        texto.setAlignment(Qt.AlignCenter)
        texto.setFont(font)
        #//////////////////////////////////////-
        
        #Menu /////////////////////////////////-
        menu = self.menuBar()
        arquivo_menu = menu.addMenu('Menu')
        action = QAction('Print!', self)
        arquivo_menu.addAction(action)
        #//////////////////////////////////////-
        
        layout.addWidget(texto)
        
        tela.setLayout(layout)
        self.setCentralWidget(tela)
   
app = QApplication()
app.setStyleSheet(load_stylesheet('dark', 'rounded'))
# app.setStyleSheet(
#     'QPushButton {\
#     background-color: #bfbfbf;\
#     border-width: 0px;\
#     border-radius: 10px;\
#     font: normal 14px;\
#     min-width: 10em;\
#     color: black;\
#     padding: 6px;}'
#     )
janela = Window()
janela.setGeometry(200, 200, 500, 400)
janela.show()
app.exec()
