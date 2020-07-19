# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 521)
        MainWindow.setStyleSheet("background-color: #e0e0e0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(0, 61, 480, 400))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("background-color: white;\n"
"border: 0;\n"
"padding: 25px\n"
"")
        self.input_text.setObjectName("input_text")
        self.output_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(481, 61, 480, 400))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.output_text.setFont(font)
        self.output_text.setStyleSheet("background-color: white;\n"
"border: 0;\n"
"padding: 25px\n"
"")
        self.output_text.setObjectName("output_text")
        self.toolbar = QtWidgets.QFrame(self.centralwidget)
        self.toolbar.setGeometry(QtCore.QRect(0, 0, 961, 60))
        self.toolbar.setStyleSheet("background-color: white;\n"
"\n"
"")
        self.toolbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolbar.setObjectName("toolbar")
        self.btn_check_lang = QtWidgets.QPushButton(self.toolbar)
        self.btn_check_lang.setGeometry(QtCore.QRect(0, 0, 480, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_check_lang.setFont(font)
        self.btn_check_lang.setStyleSheet("QPushButton {\n"
"    color: #4284f3;\n"
"    border: 0;\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d4e8fa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid #4284f3;\n"
"    background-color: white;\n"
"}")
        self.btn_check_lang.setObjectName("btn_check_lang")

        self.btn_en_lang = QtWidgets.QPushButton(self.toolbar)
        self.btn_en_lang.setGeometry(QtCore.QRect(481, 0, 180, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_en_lang.setFont(font)
        self.btn_en_lang.setStyleSheet("QPushButton {\n"
"    color: #4284f3;\n"
"    border: 0;\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d4e8fa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid #4284f3;\n"
"    background-color: white;\n"
"}")
        self.btn_en_lang.setObjectName("btn_en_lang")

        self.btn_ru_lang = QtWidgets.QPushButton(self.toolbar)
        self.btn_ru_lang.setGeometry(QtCore.QRect(661, 0, 140, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_ru_lang.setFont(font)
        self.btn_ru_lang.setStyleSheet("QPushButton {\n"
"    color: #4284f3;\n"
"    border: 0;\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d4e8fa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid #4284f3;\n"
"    background-color: white;\n"
"}")
        self.btn_ru_lang.setObjectName("btn_ru_lang")

        self.btn_de_lang = QtWidgets.QPushButton(self.toolbar)
        self.btn_de_lang.setGeometry(QtCore.QRect(801, 0, 160, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_de_lang.setFont(font)
        self.btn_de_lang.setStyleSheet("QPushButton {\n"
"    color: #4284f3;\n"
"    border: 0;\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d4e8fa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid #4284f3;\n"
"    background-color: white;\n"
"}")
        self.btn_de_lang.setObjectName("btn_de_lang")
        
        self.btn_translate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_translate.setGeometry(QtCore.QRect(0, 461, 961, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_translate.setFont(font)
        self.btn_translate.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #4284f3;\n"
"    border: 0\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #76a4f5;\n"
"    border: 0\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #4284f3;\n"
"    border-top: 2px solid #4284f3;\n"
"}")
        self.btn_translate.setObjectName("btn_translate")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_check_lang.setText(_translate("MainWindow", "ОПРЕДЕЛИТЬ ЯЗЫК"))
        self.btn_en_lang.setText(_translate("MainWindow", "АНГЛИЙСКИЙ"))
        self.btn_ru_lang.setText(_translate("MainWindow", "РУССКИЙ"))
        self.btn_de_lang.setText(_translate("MainWindow", "НЕМЕЦКИЙ"))
        self.btn_translate.setText(_translate("MainWindow", "ПЕРЕВЕСТИ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
