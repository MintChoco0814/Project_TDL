from PyQt5.QtWidgets import *


def close_Event(self, event):

    reply = QMessageBox.question(self,
                                 'Message',
                                 '프로그램을 종료하시겠습니까?',
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.Yes)

    if reply == QMessageBox.Yes: event.accept()
    else: event.ignore()