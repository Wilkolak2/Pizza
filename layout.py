# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 460)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 601, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pieBtn = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.pieBtn.setObjectName("pieBtn")
        self.gridLayout.addWidget(self.pieBtn, 2, 2, 1, 1)
        self.szyBtn = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.szyBtn.setObjectName("szyBtn")
        self.gridLayout.addWidget(self.szyBtn, 3, 2, 1, 1)
        self.kukBtn = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.kukBtn.setObjectName("kukBtn")
        self.gridLayout.addWidget(self.kukBtn, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.largeBtn = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.largeBtn.setObjectName("largeBtn")
        self.gridLayout.addWidget(self.largeBtn, 1, 2, 1, 1)
        self.smallBtn = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.smallBtn.setObjectName("smallBtn")
        self.gridLayout.addWidget(self.smallBtn, 1, 0, 1, 1)
        self.mediumBtn = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.mediumBtn.setObjectName("mediumBtn")
        self.gridLayout.addWidget(self.mediumBtn, 1, 1, 1, 1)
        self.anaBtn = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.anaBtn.setObjectName("anaBtn")
        self.gridLayout.addWidget(self.anaBtn, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 4, 2)
        self.zamBtn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.zamBtn.setObjectName("zamBtn")
        self.gridLayout.addWidget(self.zamBtn, 6, 0, 1, 3)
        self.wynik = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.wynik.setMaximumSize(QtCore.QSize(16777215, 50))
        self.wynik.setText("")
        self.wynik.setObjectName("wynik")
        self.gridLayout.addWidget(self.wynik, 7, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pieBtn.setText(_translate("Dialog", "Pieczarki"))
        self.szyBtn.setText(_translate("Dialog", "Szynka"))
        self.kukBtn.setText(_translate("Dialog", "Kukurydza"))
        self.label.setText(_translate("Dialog", "Wybierz rozmiar pizzy"))
        self.largeBtn.setText(_translate("Dialog", "Duża"))
        self.smallBtn.setText(_translate("Dialog", "Mała"))
        self.mediumBtn.setText(_translate("Dialog", "Średnia"))
        self.anaBtn.setText(_translate("Dialog", "Ananas"))
        self.label_2.setText(_translate("Dialog", "Wybierz dodatki"))
        self.zamBtn.setText(_translate("Dialog", "Zamów"))
