from PyQt5 import QtWidgets, Qt, QtCore

#Единственный верный вход датабазы

import datetime

DAY_ACTIVITY = [
    Qt.QColor(244,156,59),
    Qt.QColor(242,59,27),
    Qt.QColor(197,14,78),
    Qt.QColor(143,11,113)
]
def translate_to_datetime(what: str):
    # print(what)
    a = '%Y-%m-%d'
    return datetime.strptime(what,a).date()

def init_qdate(date: datetime.date):
    return QtCore.QDate(date)

def get_level_by_day_id(day_id: int, base: list):
    lv = base[day_id]['level']
    return DAY_ACTIVITY[lv]

def paint_day_inactivity(self, painter, rect, date):
    painter.save()
    self.brush = Qt.QBrush(QtCore.Qt.SolidPattern)
    color_of_activity = DAY_ACTIVITY[0]
    self.brush.setColor(color_of_activity)
    painter.setBrush(self.brush)
    painter.drawRect(rect)

    painter.setPen(Qt.QColor(168, 34, 3))
    painter.setFont(Qt.QFont('Bold', 10))
    painter.drawText(Qt.QRectF(rect), QtCore.Qt.TextSingleLine|QtCore.Qt.AlignCenter, str(date.day()))
    painter.restore()

def paint_day_activity(self, painter, rect, date, newExemplar):
    painter.save()
    self.brush = Qt.QBrush(QtCore.Qt.SolidPattern)
    n = newExemplar.dayColor(date.toPyDate())
    color_of_activity = DAY_ACTIVITY[n]
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
        qdates.append(init_qdate(date))
    return qdates
