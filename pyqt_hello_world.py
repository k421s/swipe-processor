import sys
import random
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys

from PySide6 import QtCore, QtWidgets, QtGui #import qt python submodules
from PyQt5.QtCore import QSize, QTimer




class MyWidget(QtWidgets.QWidget): #class extending qwidget
    def __init__(self): # python 'constructor'
        super().__init__() # COOPERATIVE MULTIPLE INHERITANCE -- MRO BUT WITH DIAMOND PROBLEMS WOO!

        # define buttons
        # self.button_a = QtWidgets.QPushButton("A")
        # self.button_a = QtWidgets.QPushButton("B")
        # self.button_a = QtWidgets.QPushButton("C")
        # self.button_a = QtWidgets.QPushButton("D")
        # self.button_a = QtWidgets.QPushButton("E")
        # self.button_a = QtWidgets.QPushButton("F")
        # self.button_a = QtWidgets.QPushButton("G")
        # self.button_a = QtWidgets.QPushButton("H")
        # self.button_a = QtWidgets.QPushButton("I")
        # self.button_a = QtWidgets.QPushButton("J")
        # self.button_a = QtWidgets.QPushButton("K")
        # self.button_a = QtWidgets.QPushButton("L")
        # self.button_a = QtWidgets.QPushButton("M")
        # self.button_a = QtWidgets.QPushButton("N")
        # self.button_a = QtWidgets.QPushButton("O")
        # self.button_a = QtWidgets.QPushButton("P")
        # self.button_a = QtWidgets.QPushButton("Q")
        # self.button_a = QtWidgets.QPushButton("R")
        # self.button_a = QtWidgets.QPushButton("S")
        # self.button_a = QtWidgets.QPushButton("T")
        # self.button_a = QtWidgets.QPushButton("U")
        # self.button_a = QtWidgets.QPushButton("V")
        # self.button_a = QtWidgets.QPushButton("W")
        # self.button_a = QtWidgets.QPushButton("X")
        # self.button_a = QtWidgets.QPushButton("Y")
        # self.button_a = QtWidgets.QPushButton("Z")
        
        self.button1 = QtWidgets.QPushButton("Click")

        #change sizing policy for the button
        self.button1.setFixedSize(50,50)
        #self.button1.setAlign
        self.button2 = QtWidgets.QPushButton("Second")
        self.button3 = QtWidgets.QPushButton("third Click Me!")
        self.button4 = QtWidgets.QPushButton("fourth Click Me!")
        self.button5 = QtWidgets.QPushButton("fifth Click Me!")
        self.button6 = QtWidgets.QPushButton("sixth Click Me!")
        

        
        # setting grid layout
        self.layout = QtWidgets.QGridLayout(self)
        
        self.layout.addWidget((self.button1), 0, 0)
        #self.button1.setFormAlignment(Qt.AlignCenter)
        self.layout.addWidget((self.button2), 0, 1)
        self.layout.addWidget((self.button3), 0, 2)
        self.layout.addWidget((self.button4), 1, 0)
        self.layout.addWidget((self.button5), 1, 1)
        self.layout.addWidget((self.button6), 1, 2)
        
       # self.button1.setAlignment(Qt.AlignBottom)


        #magic member function to choose random from greeting pool
        self.button1.clicked.connect(self.magic)

    #slot to recieve magic from button when clicked
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #initialize pyqt with no args

    #define widget characterisics
    widget = MyWidget()
    #widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())