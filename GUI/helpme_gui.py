# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpme_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(820, 325, 281, 431))
        self.widget.setAcceptDrops(False)
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ipEdit = QtWidgets.QLineEdit(self.widget)
        self.ipEdit.setGeometry(QtCore.QRect(30, 100, 51, 20))
        self.ipEdit.setObjectName("ipEdit")
        self.ipEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.ipEdit_2.setGeometry(QtCore.QRect(90, 100, 51, 20))
        self.ipEdit_2.setObjectName("ipEdit_2")
        self.ipEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.ipEdit_3.setGeometry(QtCore.QRect(150, 100, 51, 20))
        self.ipEdit_3.setObjectName("ipEdit_3")
        self.ipEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.ipEdit_4.setGeometry(QtCore.QRect(210, 100, 51, 20))
        self.ipEdit_4.setObjectName("ipEdit_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.networkEdit = QtWidgets.QLineEdit(self.widget)
        self.networkEdit.setGeometry(QtCore.QRect(30, 170, 61, 20))
        self.networkEdit.setObjectName("networkEdit")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.domainEdit = QtWidgets.QLineEdit(self.widget)
        self.domainEdit.setGeometry(QtCore.QRect(30, 230, 231, 20))
        self.domainEdit.setObjectName("domainEdit")
        self.domainButton = QtWidgets.QPushButton(self.widget)
        self.domainButton.setGeometry(QtCore.QRect(150, 170, 101, 31))
        self.domainButton.setObjectName("domainButton")
        self.connectButton = QtWidgets.QPushButton(self.widget)
        self.connectButton.setGeometry(QtCore.QRect(0, 360, 281, 31))
        self.connectButton.setObjectName("connectButton")
        self.userEdit = QtWidgets.QLineEdit(self.widget)
        self.userEdit.setGeometry(QtCore.QRect(30, 300, 231, 20))
        self.userEdit.setObjectName("userEdit")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Network Settings"))
        self.label_2.setText(_translate("MainWindow", "IP ADDRESS"))
        self.label_3.setText(_translate("MainWindow", "Network Port"))
        self.label_4.setText(_translate("MainWindow", "Domain Name"))
        self.domainButton.setText(_translate("MainWindow", "Local Domain"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.label_5.setText(_translate("MainWindow", "UserName"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
