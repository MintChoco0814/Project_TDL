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
        # self.button = QPushButton('새로운 창', self)
        # self.button.clicked.connect(self.dialog_open)
        # self.button.setGeometry(10, 10, 50, 50)  # x, y, h, w
        #
        # self.dialog = QDialog()

    def initUI(self):
        # 스테이터스 바에 날짜, 시간 표시
        datetime = QDateTime.currentDateTime()
        self.statusBar().showMessage(f"{datetime.toString(Qt.DefaultLocaleLongDate)}")

        self.setWindowTitle("To Do List")
        self.resize(500, 500)
        self.windowCenter()

        # Create a central widget and a layout for it
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Create a checkbox button
        self.button_checkbox = QPushButton('추가하기', self)
        self.button_checkbox.clicked.connect(self.create_checkbox)

        # Add the button to the layout
        layout.addWidget(self.button_checkbox)

        # delete checkboxes
        self.del_btn = QPushButton('Del CheckBox', self)
        self.del_btn.clicked.connect(self.delete_checkbox)
        layout.addWidget(self.del_btn)

        # Create a list to store the checkboxes
        self.checkboxes = []

        # Set the central widget and layout
        self.setCentralWidget(central_widget)

    def create_checkbox(self):
        text, ok = QInputDialog.getText(self, 'Checkbox Test', 'Enter Checkbox Text: ')
        if ok and text:
            checkbox = QCheckBox(text, self)
            self.checkboxes.append(checkbox)
            self.centralWidget().layout().addWidget(checkbox)

    def delete_checkbox(self):
        checkboxes_to_delete = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                checkboxes_to_delete.append(checkbox)

        for checkbox in checkboxes_to_delete:
            self.checkboxes.remove(checkbox)
            checkbox.setParent(None)

    def closeEvent(self, e):

        close_Event(self, e)

        for checkbox in self.checkboxes:
            checkbox.setParent(None)
        e.accept()

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
