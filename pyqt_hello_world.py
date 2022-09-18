import sys
import random
import os

from PySide6 import QtCore, QtWidgets, QtGui #import qt python submodules 

class MyWidget(QtWidgets.QWidget): #class extending qwidget
    def __init__(self): # python 'constructor'
        super().__init__() # COOPERATIVE MULTIPLE INHERITANCE -- MRO BUT WITH DIAMOND PROBLEMS WOO!
        
        # define buttons
        self.button1 = QtWidgets.QPushButton("Click Me!")
        self.button2 = QtWidgets.QPushButton("Second Click Me!")
        self.button3 = QtWidgets.QPushButton("third Click Me!")
        self.button4 = QtWidgets.QPushButton("fourth Click Me!")
        self.button5 = QtWidgets.QPushButton("fifth Click Me!")
        self.button6 = QtWidgets.QPushButton("sixth Click Me!")
    

        # setting grid layout
        self.layout = QtWidgets.QGridLayout(self)
        
        self.layout.addWidget((self.button1), 0, 0)
        self.layout.addWidget((self.button2), 0, 1)
        self.layout.addWidget((self.button3), 0, 2)
        self.layout.addWidget((self.button4), 1, 0)
        self.layout.addWidget((self.button5), 1, 1)
        self.layout.addWidget((self.button6), 1, 2)
        

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