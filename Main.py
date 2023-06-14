import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


        self.button = QPushButton('새로운 창', self)
        self.button.clicked.connect(self.dialog_open)
        self.button.setGeometry(10, 10, 200, 50)

        self.dialog = QDialog()

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.resize(500, 500)
        self.windowCenter()

        self.button = QPushButton('새로운 창', self)
        self.button.clicked.connect(self.dialog_open)
        self.button.setGeometry(10, 10, 200, 50)

        self.dialog = QDialog()




    def dialog_open(self):

        btnDialog = QPushButton("확인", self.dialog)
        btnDialog.move(100, 100)
        btnDialog.clicked.connect(self.dialog_close)

        self.dialog.setWindowTitle("Sub Window")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(300, 200)
        self.windowCenter()
        self.dialog.show()

    def dialog_close(self):
        self.dialog.close()


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



def main():

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
