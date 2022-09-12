import os
import sys

from PySide6.QtCore import QRect, QTimer, QObject, QPoint
from PySide6.QtGui import QGuiApplication, QRegion
from PySide6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget

#source: https://felgo.com/doc/qt/qtvirtualkeyboard-basic-example/
# original keyboard https://stackoverflow.com/questions/71566198/resize-move-and-hide-virtual-keyboard-pyside6
# https://www.pythonfixing.com/2022/02/fixed-using-pyqt5-virtual-keyboard-in.html


class KeyboardManager:
    def __init__(self):
        self._keyboard_window = None
        self.input_method.visibleChanged.connect(self._handle_visible_changed)

    @property
    def input_method(self):
        input_method = QGuiApplication.inputMethod()
        if input_method is None:
            raise RuntimeError("QGuiApplication.inputMethod() is None")
        return input_method

    @property
    def keyboard_window(self):
        return self._keyboard_window

    def _handle_visible_changed(self):
        for w in QGuiApplication.allWindows():
            if w.metaObject().className() == "QtVirtualKeyboard::InputView":
                if self._keyboard_window != w:
                    if self._keyboard_window is not None:
                        self._keyboard_window.disconnect(self._handle_destroyed)
                    w.destroyed.connect(self._handle_destroyed)
                    self._keyboard_window = w
                return
        self._keyboard_window = None

    def _handle_destroyed(self):
        self._keyboard_window = None
        


def main():
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    app = QApplication(sys.argv)

    keyboard_manager = KeyboardManager()

    w = QWidget()
    le = QLineEdit()
    lay = QVBoxLayout(w)
    lay.addWidget(le)
    lay.addStretch()
    w.show()
    
    keyboard_manager.input_method.setVisible(
            not keyboard_manager.input_method.isVisible()
        )

    sys.exit(app.exec())


if __name__ == "__main__":
    main()