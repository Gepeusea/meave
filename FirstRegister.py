import sys
from PyQt5 import Qt, QtCore, QtWidgets
from uis.GlobalSettings import Ui_MainWindow

class EditGlobalSettings(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(EditGlobalSettings, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_2.setText('Самый маленький порог продуктивности')
        self.ui.label_3.setText('Средний порог продуктивности')
        self.ui.label_4.setText('Самый большой порог продуктивности')
        self.ui.buttons.accepted.connect(self.accept)

    def accept(self): # функция порожков
        val1, val2, val3 = self.ui.spinBox.value(), self.ui.spinBox_2.value(), self.ui.spinBox_3.value()
        print(val1, val2, val3)
