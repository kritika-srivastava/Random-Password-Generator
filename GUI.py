
#C:\Users\Kritika\Desktop\VSC\python\Random-Password-Generator\GUI.py
#Kritika Srivastava
#April 18, 2020
#Python code to link and interact with the GUI

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

import random
import string

qtcreator_file  = "MainWindow.ui" # Enter your .ui file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Press_This_Key.clicked.connect(self.RandomNo)
    
    def RandomNo(self):
        str_len = int(self.input.value())
        def randomString(stringLength):
                letters = string.ascii_letters
                return ''.join(random.choice(letters) for i in range(stringLength))
        out=randomString(str_len)
        
        self.Output_Browser.setText(out)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())