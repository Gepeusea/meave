from PyQt5 import QtWidgets, Qt, QtCore

#Единственный верный вход датабазы

import datetime

def translate_to_datetime(what: str):
    a = '%Y-%m-%d'
    return datetime.strptime(what,a).date()

def paint_day_activity(self, painter, rect, date, newExemplar):
    painter.save()
    self.brush = Qt.QBrush(QtCore.Qt.SolidPattern)
    color_of_activity = newExemplar.dayColor(date.toPyDate())
    self.brush.setColor(color_of_activity)
    painter.setBrush(self.brush)
    painter.drawRect(rect)

    painter.setPen(Qt.QColor(250,250,250))
    painter.setFont(Qt.QFont('Bold', 13))
    painter.drawText(Qt.QRectF(rect), QtCore.Qt.TextSingleLine|QtCore.Qt.AlignCenter, str(date.day()))
    painter.restore()

def translate_datetime_to_qdate(based_on_what: list):
    qdates = []
    for element in based_on_what:
        date = translate_to_datetime(element[0])
        qdates.append(QtCore.QDate(date))
    return qdates
