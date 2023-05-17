from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])

    Form, Window = uic.loadUiType("uibd.ui")
    window = Window()
    form = Form()

    form.setupUi(window)
    window.show()
    app.exec_()
