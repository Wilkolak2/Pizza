import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.button_click = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.zamBtn.clicked.connect(self.calculate)
        self.show()


    def calculate(self):
        size = "none"
        dodatki = []
        if self.ui.smallBtn.isChecked():
            size = "mała"
        elif self.ui.mediumBtn.isChecked():
            size = "średnia"
        elif self.ui.largeBtn.isChecked():
            size = "duza"

        if self.ui.pieBtn.isChecked():
            dodatki.append("pieczarki")
        if self.ui.szyBtn.isChecked():
            dodatki.append("szynka")
        if self.ui.kukBtn.isChecked():
            dodatki.append("kukurydza")
        if self.ui.anaBtn.isChecked():
            dodatki.append("ananas")

        if size != "none":
            self.ui.wynik.setText(f'Rozmiar twojej pizzy to: {size} , dodatki: {dodatki}')
        else:
            self.ui.wynik.setText("nie wybrano rozmiaru")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())