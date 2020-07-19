import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from googletrans import Translator



class Lang():
    def __init__(self):
        self.selected_language = ''

    def set_lang(self, selected_language):
        self.selected_language = selected_language
    


class TranslateText(QtWidgets.QMainWindow):
    def __init__(self):
        super(TranslateText, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Translator') 
        self.ui.btn_translate.clicked.connect(self.translate)
        self.ui.btn_check_lang.setDown(True)
        
        self.ui.btn_en_lang.clicked.connect(lambda: lang.set_lang('en'))
        self.ui.btn_ru_lang.clicked.connect(lambda: lang.set_lang('ru'))
        self.ui.btn_de_lang.clicked.connect(lambda: lang.set_lang('de'))

    def translate(self):
        input_text = self.ui.input_text.toPlainText()
        translated_text = translator.translate(input_text, dest=f'{lang.selected_language}')        
        self.ui.output_text.setPlainText(translated_text.text)    

if __name__ == '__main__':
    lang = Lang()
    translator = Translator()      
    app = QtWidgets.QApplication([])
    application = TranslateText()
    application.show()
    
    sys.exit(app.exec())
