from helpme_gui import *
import requests, time
from PyQt5 import QtCore, QtGui, QtWidgets
import threading    #ADDED

def ipInit(self):
    self.groupEdit = [self.ipEdit, self.ipEdit_2, self.ipEdit_3, self.ipEdit_4, self.networkEdit]
    self.ipEdit.setText("127")
    self.ipEdit_2.setText("0")
    self.ipEdit_3.setText("0")
    self.ipEdit_4.setText("1")
    self.networkEdit.setText("5000")
    for i in range(0,5):
        self.groupEdit[i].textEdited.connect(self.ipAutoComplete)
    self.domainEdit.setText("http://127.0.0.1:5000")
    self.domainButton.clicked.connect(self.ipInit)
    self.connectButton.clicked.connect(self.ipConnect)

def ipConnect(self):
    self.url = self.domainEdit.text()
    self.username = self.userEdit.text()
    data = {'username': self.username}
    requests.post(self.url, json = data)
    print('Complete')
    self.stackedWidget.setCurrentIndex(1)
    t = threading.Thread(target=self.refresh, name="[Daemon]", args=())
    t.setDaemon(True)
    t.start()


def ipAutoComplete(self):
    textArray = 'http://'
    for i in range(0,5):
        textArray += self.groupEdit[i].text()
        if i < 3:
            textArray += '.'
        elif i == 3:
            textArray += ':'
    self.domainEdit.setText(textArray)

def refresh(self):
    while True:
        linker = self.url + '/read'
        req = requests.get(linker)
        html = req.text
        html=html.split(':')
        print(html)
        time.sleep(5)

Ui_MainWindow.ipInit = ipInit
Ui_MainWindow.ipAutoComplete = ipAutoComplete
Ui_MainWindow.ipConnect = ipConnect
Ui_MainWindow.refresh = refresh

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.ipInit()
    sys.exit(app.exec_())