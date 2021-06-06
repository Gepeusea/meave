#!/usr/bin/python

import sys
from PyQt5 import QtWidgets, Qt, QtCore
from qss import BLACK_STACKOVERFLOW
from uis.LoadScreenFromMainWindow import Ui_LoadScreen
from uis.GlobalSettings import Ui_MainWindow

#import mymodules
from OpenTaskManager import TaskManager #Это ошкошечко в котором есть все задчи на день

import datetime
import datedrawer

counter = 0
class LoadScreen(QtWidgets.QMainWindow):

    def __init__(self, newExemplar, *args, **kwargs):
        super(LoadScreen, self).__init__(*args, **kwargs)
        self.ui = Ui_LoadScreen()
        self.ui.setupUi(self)
        self.newExemplar = newExemplar

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = Qt.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(Qt.QColor(100,100,100,60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        #timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(10)

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            if self.newExemplar.usersGrades == []:
                self.main = EditGlobalSettings(self.newExemplar)
                self.main.setStyleSheet(BLACK_STACKOVERFLOW)
                self.main.resize(500, 450)
                self.main.show()
            else: 
                self.main = Calendarik(self.newExemplar)
            self.main.setStyleSheet(BLACK_STACKOVERFLOW)
            self.main.resize(500, 450)
            self.main.show()
            self.close()
        counter += 1


class EditGlobalSettings(QtWidgets.QMainWindow):

    def __init__(self, newExemplar, *args, **kwargs):
        super(EditGlobalSettings, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_2.setText('Самый маленький порог продуктивности')
        self.ui.label_3.setText('Средний порог продуктивности')
        self.ui.label_4.setText('Самый большой порог продуктивности')
        self.ui.buttons.accepted.connect(self.accept)
        self.newExemplar = newExemplar

    def accept(self):
        val1, val2, val3 = self.ui.spinBox.value(), self.ui.spinBox_2.value(), self.ui.spinBox_3.value()
        self.newExemplar.usersGrades = [val1/10, val2/10, val3/10]
        self.main = Calendarik(self.newExemplar)
        self.main.setStyleSheet(BLACK_STACKOVERFLOW)
        self.main.resize(500, 450)
        self.main.show()
        self.close()


class Calendarik(QtWidgets.QCalendarWidget):

    def __init__(self, newExemplar, *args, **kwargs):
        super(Calendarik, self).__init__(*args, **kwargs)
        self.setVerticalHeaderFormat(self.NoVerticalHeader)
        self.clicked.connect(self.button_clicked)
        self.newExemplar = newExemplar

    def paintCell(self, painter, rect, date: QtCore.QDate): #date is <class 'PyQt5.QtCore.QDate'>
        painter.setRenderHint(Qt.QPainter.Antialiasing, True)
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)

        rect = Qt.QRectF(rect)
        bordersize = 10

        path = Qt.QPainterPath()
        rect.adjust(bordersize/2, bordersize/2, -bordersize/2, -bordersize/2)
        path.addRoundedRect(rect, 10, 10)

        painter.setClipPath(path)
        painter.fillPath(path, painter.brush())
        painter.strokePath(path, painter.pen())

        datedrawer.paint_day_activity(self, painter, rect, date, self.newExemplar)

    def getTasks(self, date):
        massive = []
        tDict = self.newExemplar.checkUp(date)
        
        for i in range(len(tDict['allEvents'])):
            massive.append(tDict['allEvents'][i])
        return massive

    def button_clicked(self, date: QtCore.QDate):
        tasks_in_day = self.getTasks(date.toPyDate()) #calendar data
        self.taskmanager = TaskManager(date.toPyDate(), self.newExemplar, tasks = tasks_in_day)
        self.taskmanager.show()

# Без лоадскрина
# if __name__ == '__main__':
#     app = Qt.QApplication(sys.argv)
#     app.setStyleSheet(BLACK_STACKOVERFLOW)
#     window = Calendarik()
#     window.resize(500, 450)
#     window.show()
#     sys.exit(app.exec_())

# if not file: открыть окошко с порогами
# if __name__ == '__main__':
#     app = Qt.QApplication(sys.argv)
#     window = LoadScreen()
#     window.show()
#     sys.exit(app.exec_())
