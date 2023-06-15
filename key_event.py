from PyQt5.QtCore import *


def keyEvent(self, event):
    if event.modifiers() & Qt.ControlModifier:
        if event.key() == Qt.Key_W:
            self.close()
