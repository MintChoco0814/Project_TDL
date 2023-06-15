from PyQt5.QtWidgets import *


def widget_center(dialog):
    qr = dialog.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    dialog.move(qr.topLeft())
