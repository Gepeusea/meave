#!/usr/bin/python

import sys
from PyQt5 import QtWidgets, Qt, QtCore
from qss import BLACK_STACKOVERFLOW
from uis.LoadScreenFromMainWindow import Ui_LoadScreen

#import mymodules
from OpenTaskManager import TaskManager #Это ошкошечко в котором есть все задчи на день
from FirstRegister import EditGlobalSettings #порожки

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
            self.main = Calendarik(self.newExemplar)
            self.main.setStyleSheet(BLACK_STACKOVERFLOW)
            self.main.resize(500, 450)
            self.main.show()
            self.close()
        counter += 1


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
        # y, m, d = date.year, date.month, date.day
        
        for i in range(len(tDict['allEvents'])-1):
            massive.append(tDict['allEvents'][i])
        # print('noo',y,m,d)
        print(tDict)
        print(massive)
        return massive

    def button_clicked(self, date: QtCore.QDate):
        tasks_in_day = self.getTasks(date.toPyDate()) #calendar data
        print('at first',type(tasks_in_day))
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