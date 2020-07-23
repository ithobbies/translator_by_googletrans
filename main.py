import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator



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
"QPushButton:checked {\n"                          
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
"QPushButton:checked {\n"
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
"QPushButton:checked {\n"
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



class Lang(QtWidgets.QWidget):                                       
    def __init__(self, parent=None):                                
        super(Lang, self).__init__(parent)                           
        
        self.parent = parent                                         
        
        self.selected_language = ''

    def set_lang(self, selected_language):
        self.selected_language = selected_language

        if self.parent.ui.btn_en_lang.isChecked() and selected_language == 'en':
            self.parent.ui.btn_en_lang.setDown(True)
            if self.parent.ui.btn_ru_lang.isChecked(): self.parent.ui.btn_ru_lang.setChecked(False)
            if self.parent.ui.btn_de_lang.isChecked(): self.parent.ui.btn_de_lang.setChecked(False)

        if self.parent.ui.btn_ru_lang.isChecked() and selected_language == 'ru':
            self.parent.ui.btn_ru_lang.setDown(True)
            if self.parent.ui.btn_en_lang.isChecked(): self.parent.ui.btn_en_lang.setChecked(False) 
            if self.parent.ui.btn_de_lang.isChecked(): self.parent.ui.btn_de_lang.setChecked(False) 
            
        if self.parent.ui.btn_de_lang.isChecked() and selected_language == 'de':
            self.parent.ui.btn_de_lang.setDown(True)
            if self.parent.ui.btn_en_lang.isChecked(): self.parent.ui.btn_en_lang.setChecked(False) 
            if self.parent.ui.btn_ru_lang.isChecked(): self.parent.ui.btn_ru_lang.setChecked(False)             
      
    

class TranslateText(QtWidgets.QMainWindow):
    def __init__(self):
        super(TranslateText, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.lang = Lang(self)                                         
        
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Translator') 
        self.ui.btn_translate.clicked.connect(self.translate)
        self.ui.btn_check_lang.setDown(True)
        
        self.ui.btn_en_lang.setCheckable(True)
        self.ui.btn_ru_lang.setCheckable(True)
        self.ui.btn_de_lang.setCheckable(True)

        self.ui.btn_en_lang.clicked.connect(lambda: self.lang.set_lang('en'))  
        self.ui.btn_ru_lang.clicked.connect(lambda: self.lang.set_lang('ru'))
        self.ui.btn_de_lang.clicked.connect(lambda: self.lang.set_lang('de'))

    def translate(self):
        input_text = self.ui.input_text.toPlainText()
      
        if input_text and self.lang.selected_language:
            translated_text = translator.translate(input_text, dest=f'{self.lang.selected_language}')        
            self.ui.output_text.setPlainText(translated_text.text)    
        else: 
            msg = QtWidgets.QMessageBox.information(
                    self, 
                    'ВНИМАНИЕ', 
                    'Введите текст для перевода \nи выберите язык, \nна который будем переводить!')        



if __name__ == '__main__':
    translator = Translator()      
    app = QtWidgets.QApplication([])
    application = TranslateText()
    application.show()
    sys.exit(app.exec())