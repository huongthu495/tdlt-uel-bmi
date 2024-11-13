# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 230, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(400, 430, 111, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../LearnQPushButton/images/8664836_id_card_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonClose.setIcon(icon)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 370, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 160, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditWeight = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditWeight.setGeometry(QtCore.QRect(240, 150, 271, 31))
        self.lineEditWeight.setObjectName("lineEditWeight")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 160, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 310, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButtonCalculate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(210, 430, 111, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../LearnQPushButton/images/8664826_keyboard_computer_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCalculate.setIcon(icon1)
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 50, 481, 61))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.labelBMI = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelBMI.setGeometry(QtCore.QRect(240, 300, 271, 16))
        self.labelBMI.setObjectName("labelBMI")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 230, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.labelComment = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelComment.setGeometry(QtCore.QRect(240, 370, 271, 16))
        self.labelComment.setObjectName("labelComment")
        self.lineEditHeight = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditHeight.setGeometry(QtCore.QRect(240, 220, 271, 31))
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 300, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "(CM)"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
        self.label_8.setText(_translate("MainWindow", "Comment:"))
        self.label.setText(_translate("MainWindow", "(Kg)"))
        self.label_2.setText(_translate("MainWindow", "Weight:"))
        self.label_7.setText(_translate("MainWindow", "kg/m2"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Calculate"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">BMI Application</span></p></body></html>"))
        self.labelBMI.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Height:"))
        self.labelComment.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "BMI:"))