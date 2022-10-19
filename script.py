from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                               QPushButton, QWidget)
from qdarktheme import load_stylesheet

font = QFont()
font.setPixelSize(24)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        tela = QWidget()
        layout = QGridLayout()

        #Botões ///////////////////////////////-
        but0 = QPushButton('0')
        but1 = QPushButton('1')
        but2 = QPushButton('2')
        but3 = QPushButton('3')
        but4 = QPushButton('4')
        but5 = QPushButton('5')
        but6 = QPushButton('6')
        but7 = QPushButton('7')
        but8 = QPushButton('8')
        but9 = QPushButton('9')
        #//////////////////////////////////////-


        #Texto ////////////////////////////////-
        texto = QLabel('-')
        texto.setFont(font)
        texto.setAlignment(Qt.AlignCenter)
        #//////////////////////////////////////-
        
        
        layout.addWidget(texto, 0, 0)
        layout.addWidget(but1, 1, 0)


        tela.setLayout(layout)
        self.setCentralWidget(tela)
   
app = QApplication()
app.setStyleSheet(load_stylesheet('dark', 'rounded'))
janela = Window()
janela.setGeometry(200, 200, 500, 400)
janela.show()
app.exec()
