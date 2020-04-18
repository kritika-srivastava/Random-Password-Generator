# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(561, 396))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(580, 0, 20, 361))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 441, 21))
        self.label.setObjectName("label")
        self.PasswordOutput = QtWidgets.QFrame(self.centralwidget)
        self.PasswordOutput.setGeometry(QtCore.QRect(69, 160, 451, 111))
        self.PasswordOutput.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PasswordOutput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PasswordOutput.setObjectName("PasswordOutput")
        self.pushButton = QtWidgets.QPushButton(self.PasswordOutput)
        self.pushButton.setGeometry(QtCore.QRect(110, 20, 221, 61))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 250, 451, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(390, 50, 64, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 50, 221, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(50, 120, 42, 22))
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuSimple_Password = QtWidgets.QMenu(self.menubar)
        self.menuSimple_Password.setObjectName("menuSimple_Password")
        self.menuMedium_Password_Level_2 = QtWidgets.QMenu(self.menubar)
        self.menuMedium_Password_Level_2.setObjectName("menuMedium_Password_Level_2")
        self.menuDifficult_Password_Level_3 = QtWidgets.QMenu(self.menubar)
        self.menuDifficult_Password_Level_3.setObjectName("menuDifficult_Password_Level_3")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAlphabets_Symbols_numbers = QtWidgets.QAction(MainWindow)
        self.actionAlphabets_Symbols_numbers.setObjectName("actionAlphabets_Symbols_numbers")
        self.actionSmall_Alphabets = QtWidgets.QAction(MainWindow)
        self.actionSmall_Alphabets.setObjectName("actionSmall_Alphabets")
        self.actionCapital_Alphabets = QtWidgets.QAction(MainWindow)
        self.actionCapital_Alphabets.setObjectName("actionCapital_Alphabets")
        self.actionMixture_of_Alphabets = QtWidgets.QAction(MainWindow)
        self.actionMixture_of_Alphabets.setObjectName("actionMixture_of_Alphabets")
        self.actionAlphabets_and_Numbers = QtWidgets.QAction(MainWindow)
        self.actionAlphabets_and_Numbers.setObjectName("actionAlphabets_and_Numbers")
        self.menuSimple_Password.addSeparator()
        self.menuSimple_Password.addAction(self.actionSmall_Alphabets)
        self.menuSimple_Password.addAction(self.actionCapital_Alphabets)
        self.menuSimple_Password.addAction(self.actionMixture_of_Alphabets)
        self.menuMedium_Password_Level_2.addAction(self.actionAlphabets_and_Numbers)
        self.menuDifficult_Password_Level_3.addSeparator()
        self.menuDifficult_Password_Level_3.addAction(self.actionAlphabets_Symbols_numbers)
        self.menubar.addAction(self.menuSimple_Password.menuAction())
        self.menubar.addAction(self.menuMedium_Password_Level_2.menuAction())
        self.menubar.addAction(self.menuDifficult_Password_Level_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random Password Generator(By KriSh)"))
        self.label.setText(_translate("MainWindow", "Note :You can select the level of difficulty of password from the above menu."))
        self.pushButton.setText(_translate("MainWindow", "Press This Key for Random Password"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Enter the number of words in the password"))
        self.menuSimple_Password.setTitle(_translate("MainWindow", "(Level 1)Easy Password"))
        self.menuMedium_Password_Level_2.setTitle(_translate("MainWindow", "(Level 2)Medium Password"))
        self.menuDifficult_Password_Level_3.setTitle(_translate("MainWindow", "(Level 3)Difficult Password "))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAlphabets_Symbols_numbers.setText(_translate("MainWindow", "Alphabets,Numbers and Special Characters"))
        self.actionSmall_Alphabets.setText(_translate("MainWindow", "Small Alphabets"))
        self.actionCapital_Alphabets.setText(_translate("MainWindow", "Capital Alphabets"))
        self.actionMixture_of_Alphabets.setText(_translate("MainWindow", "Mixture of Alphabets"))
        self.actionAlphabets_and_Numbers.setText(_translate("MainWindow", "Alphabets and Numbers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
