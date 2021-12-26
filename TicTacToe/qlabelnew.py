from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

class QLabelNew(QtWidgets.QLabel):
    clicked = pyqtSignal()
    def mousePressEvent(self, ev) -> None:
        self.clicked.emit()
