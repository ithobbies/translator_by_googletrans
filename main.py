import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from googletrans import Translator



class TranslateText(QtWidgets.QMainWindow):
    def __init__(self):
        super(TranslateText, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Google Translate') 
        self.ui.btn_translate.clicked.connect(self.translate)
        self.ui.btn_check_lang.setDown(True)
        
        self.ui.btn_eng_lang.clicked.connect(self.translate_into_en)
        self.ui.btn_ru_lang.clicked.connect(self.translate_into_ru)
        self.ui.btn_ge_lang.clicked.connect(self.translate_into_de)
    
    def translate_into_en(self):
        global selected_language
        selected_language = 'en'
    
    def translate_into_ru(self):
        global selected_language
        selected_language = 'ru'

    def translate_into_de(self):
        global selected_language
        selected_language = 'de'

    def translate(self):
        global selected_language
        input_text = self.ui.input_text.toPlainText()
        translated_text = translator.translate(input_text, dest=f'{selected_language}')        
        self.ui.output_text.setPlainText(translated_text.text)    

selected_language = ''
translator = Translator()      
app = QtWidgets.QApplication([])
application = TranslateText()
application.show()
 
sys.exit(app.exec())
