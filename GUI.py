# Kritika Srivastava
# April 19, 2020
# Final GUI code 

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

import random
import string

qtcreator_file = "MainWindow.ui"  # Enter your .ui file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Calling each menubar to connect to its method
        self.actionSmall_Letters.triggered.connect(
            lambda: self.Small_Letters())
        self.actionCapital_Letters.triggered.connect(
            lambda: self.Capital_Letters())
        self.actionMixture_of_Alphabets.triggered.connect(
            lambda: self.Mixture_of_Alphabets())
        self.actionNumbers.triggered.connect(lambda: self.Numbers())
        self.actionAlphabets_and_Numbers.triggered.connect(
            lambda: self.Alphabets_and_Numbers())
        self.actionAlphabets_Numbers_and_Symbols.triggered.connect(
            lambda: self.Alphabets_Numbers_and_Symbols())

    def Mixture_of_Alphabets(self):
        # Connection to the actual function
        self.Press_This_Key.clicked.connect(self.RandomNo)

    def RandomNo(self):
        # Taking the input for number of words
        str_len = int(self.input.value())

        def randomString(stringLength):
            # Specifying the samplespace for password generation
            letters = string.ascii_letters
            return ''.join(random.choice(letters) for i in range(stringLength))
        out = randomString(str_len)
        self.Output_Browser.setText(out)
#  Rest all the methods have been designed in the same way

    def Small_Letters(self):
        self.Press_This_Key.clicked.connect(self.RandomNo1)

    def RandomNo1(self):
        str_len = int(self.input.value())

        def randomString(stringLength):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))
        out = randomString(str_len)
        self.Output_Browser.setText(out)

    def Capital_Letters(self):
        self.Press_This_Key.clicked.connect(self.RandomNo2)

    def RandomNo2(self):
        str_len = int(self.input.value())

        def randomString(stringLength):
            letters = string.ascii_uppercase
            return ''.join(random.choice(letters) for i in range(stringLength))
        out = randomString(str_len)
        self.Output_Browser.setText(out)

    def Numbers(self):
        self.Press_This_Key.clicked.connect(self.RandomNo3)

    def RandomNo3(self):
        str_len = int(self.input.value())

        def randomString(stringLength):
            letters = string.digits
            return ''.join(random.choice(letters) for i in range(stringLength))
        out = randomString(str_len)
        self.Output_Browser.setText(out)

    def Alphabets_and_Numbers(self):
        self.Press_This_Key.clicked.connect(self.RandomNo4)

    def RandomNo4(self):
        str_len = int(self.input.value())

        def randomString(stringLength):
            letters = string.ascii_letters + string.digits
            return ''.join(random.choice(letters) for i in range(stringLength))
        out = randomString(str_len)
        self.Output_Browser.setText(out)

    def Alphabets_Numbers_and_Symbols(self):
        self.Press_This_Key.clicked.connect(self.RandomNo5)

    def RandomNo5(self):
        str_len = int(self.input.value())

        def randomString(stringLength):
            letters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(letters) for i in range(stringLength))
        out = randomString(str_len)
        self.Output_Browser.setText(out)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
