import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.resize(500, 500)
        self.windowCenter()
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', '프로그램을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes: event.accept()
        else: event.ignore()


    def keyPressEvent(self, event):

        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_W:
                self.close() # 화면 닫기 단축기 ctrl + w

    def windowCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # 화면 중간으로 오게하기
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
