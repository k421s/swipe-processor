import sys
import random
import os

from PySide6 import QtCore, QtWidgets, QtGui #import qt python submodules 

class MyWidget(QtWidgets.QWidget): #class extending qwidget
    def __init__(self): # python 'constructor'
        super().__init__() # COOPERATIVE MULTIPLE INHERITANCE -- MRO BUT WITH DIAMOND PROBLEMS WOO!

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"] #greeting pool

        #add and align buttons
        self.button = QtWidgets.QPushButton("Click Me!")
        self.text = QtWidgets.QLabel("Hello World", alignment = QtCore.Qt.AlignRight)
        
        #attempting to add a 2nd button - it wont do anything yet
        self.button2 = QtWidgets.QPushButton("Second Click Me!")
        self.button3 = QtWidgets.QPushButton("third Click Me!")
        self.button4 = QtWidgets.QPushButton("fourth Click Me!")
        self.button5 = QtWidgets.QPushButton("fifth Click Me!")

        # layout layer
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        
        #adding new button to layer:
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)


        #magic member function to choose random from greeting pool
        self.button.clicked.connect(self.magic)

    #slot to recieve magic from button when clicked
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #initialize pyqt with no args

    #define widget characterisics
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())