import sys
import datetime
from PyQt5 import Qt, QtCore, QtWidgets
from uis.TaskEdit import Ui_MainWindow

html_text1 = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }'
html_text2 = '</style></head><body style=" font-family:"MS Shell Dlg 2"; font-size:8pt; font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">{}</span></p></body></html>'

class EditTaskClass(QtWidgets.QMainWindow):

	def __init__(self, newExemplar: object, date: datetime.datetime, taskNumber= None, text = None, level = None, flag = False, *args, **kwargs):
		super(EditTaskClass, self).__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.label.setText(f'<html><head/><body><p><span style=" font-size:48pt;">{date}</span></p></body></html>') #Date
		if not text and not level:
			html_text = html_text1 + html_text2.format('there is nothing here yet')
		else:
			html_text = html_text1 + html_text2.format(text) 
		self.ui.current_text.setText(html_text)
		self.ui.current_level.setValue(level or 0)

		#"апи"
		self.ui.buttons.accepted.connect(self.accept)
		self.ui.buttons.rejected.connect(self.reject)

		self.taskNumber = taskNumber
		self.flag = flag
		self.newExemplar = newExemplar
		self.date = date

	def accept(self):
		print(f'Accepted info: {self.ui.current_text.toPlainText()}, {self.ui.current_level.value()}')
		if self.taskNumber == None:
			self.newExemplar.newTask(self.ui.current_text.toPlainText(), self.ui.current_level.value(), self.date)
		else: 
			self.newExemplar.changeTask(self.taskNumber, self.ui.current_text.toPlainText(), self.ui.current_level.value(), self.flag, self.date)
		self.close()

	def reject(self):
		self.close()