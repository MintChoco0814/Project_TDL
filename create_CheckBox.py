from PyQt5.QtWidgets import *


def checkbox_create(dialog):
    text, ok = QInputDialog.getText(dialog, 'Checkbox Text', 'List 추가하기 : ')
    if ok and text:
        checkbox = QCheckBox(text, dialog)
        dialog.centralWidget().layout().addWidget(checkbox)
