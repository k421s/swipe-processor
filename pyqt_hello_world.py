import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui #import qt python submodules 

class MyWidget(QtWidgets.QWidget): #class extending qwidget
    def __init__(self): # python 'constructor'
        super().__init__() # COOPERATIVE MULTIPLE INHERITANCE -- MRO BUT WITH DIAMOND PROBLEMS WOO!

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"] #greeting pool

        #add and align buttons
        self.button = QtWidgets.QPushButton("Click Me!")
        self.text = QtWidgets.QLabel("Hello World", alignment = QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

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