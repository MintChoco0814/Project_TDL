import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from close_event import close_Event
from key_event import keyEvent
from window_center import widget_center


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        # 두 번째 나타내는 버튼 만들기
        self.button = QPushButton('새로운 창', self)
        self.button.clicked.connect(self.dialog_open)
        self.button.setGeometry(10, 10, 50, 50) # x, y, h, w

        self.dialog = QDialog()

    def initUI(self):
        # 스테이터스 바에 날짜, 시간 표시
        datetime = QDateTime.currentDateTime()
        self.statusBar().showMessage(f"{datetime.toString(Qt.DefaultLocaleLongDate)}")

        self.setWindowTitle("To Do List")
        self.resize(500, 500)
        self.windowCenter()

    def dialog_open(self):

        btnDialog = QPushButton("확인", self.dialog)
        btnDialog.move(100, 100)
        btnDialog.clicked.connect(self.dialog_close)

        # 두 번째 창 만들기
        self.dialog.setWindowTitle("Sub Window")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(300, 200)
        self.windowCenter()
        self.dialog.show()

    def dialog_close(self):
        # 두 번째 창 닫기.
        self.dialog.close()

    def closeEvent(self, e):
        close_Event(self, e)

    def keyPressEvent(self, event):
        # 화면 닫기 단축기 ctrl + w
        keyEvent(self, event)

    def windowCenter(self):
        # 화면 중간으로 오게하기
        widget_center(self)


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
