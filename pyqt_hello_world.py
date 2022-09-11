import sys
import random

from PySide6 import QtCore, QtWidgets, QtGui

# class named MyWidget - extending QTWidget 
class MyWidget(QtWidgets.QWidget):
    def __init__(self): #constructor
        super().__init__() # access to methods in super class of qtwidgets.qwidget

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        
        self.button = QtWidgets.QPushButton("Click Me!")
        self.text - QtWidgets.Qlabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QvBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        
        self.button.clicked.connect(self.magic)
        
        @QtCore.Slot()
        def magic(self):
            self.text.setText(random.choice(self.hello))
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication([]) 
    
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())
    
    