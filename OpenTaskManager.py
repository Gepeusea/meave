import sys
import datetime
from PyQt5 import QtWidgets, Qt, QtCore

from uis.OpenTask import Ui_MainWindow

from datedrawer import translate_datetime_to_qdate
from EditTask import EditTaskClass

LastStateRole = QtCore.Qt.UserRole

class ViewTaskIn(Qt.QWidget):

    def __init__(self, date, tasks, newExemplar):
        super().__init__()
        layout = Qt.QHBoxLayout(self)
        self.tasks = tasks
        print('this is tasks: ', tasks)
        self.date = date
        self.table = Qt.QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(2)
        self.table.setShowGrid(0)

        self.table.visualColumn(0)
        self.table.visualRow(0)
        self.table.verticalHeader().setVisible(0)
        self.table.horizontalHeader().setVisible(0)
        self.table.setShowGrid(0)

        self.newExemplar = newExemplar

        layout.addWidget(self.table)
        self.table.cellChanged.connect(self.onCellChanged)

    def create_1(self, row: int, date: datetime.datetime):
        item = QtWidgets.QTableWidgetItem()
        item.setText(self.tasks[row]['note'])
        #item.setText('<html><head/><body><p align="center"><span style=" font-size:36pt;">{text}</span></p></body></html>')
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        if self.tasks[row]['flag']:
            item.setCheckState(QtCore.Qt.CheckState(2))
        else:
            item.setCheckState(QtCore.Qt.CheckState(0))
        item.setData(LastStateRole, item.checkState())
        item.setTextAlignment(QtCore.Qt.AlignLeft);

        self.table.setItem(row, 0, item)
        self.table.resizeColumnsToContents()
        #self.table.setSizeHint(QSize(320, 200))

        btn_edit = QtWidgets.QPushButton('✏️')
        btn_edit.setGeometry(200, 150, 100, 40)
        btn_edit.clicked.connect(self.deleteClicked)
        self.table.setCellWidget(row, 1, btn_edit)

    @QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        taskNumber = self.table.indexAt(button.pos()).row()
        #self.table.removeRow(row)
        print('eto row', taskNumber) # ВЕРНЕТСЯ НОМЕР ЗАДАЧИ
        task_info = self.tasks[taskNumber]
        print('TASK INFO', task_info)
        self.task = EditTaskClass(taskNumber, self.newExemplar, self.date, task_info['note'], task_info['grade'], task_info['flag'])
        self.task.show()

    def onCellChanged(self, row, column):
         item = self.table.item(row, column)
         lastState = item.data(LastStateRole)
         currentState = item.checkState()
         if currentState != lastState:
            self.newExemplar.changeFlag(self.date, row)


class TaskManager(QtWidgets.QMainWindow):

    def __init__(self, date = None, newExemplar = None, tasks = None, *args, **kwargs):
        self.date = date
        self.newExemplar = newExemplar
        super(TaskManager, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        container = ViewTaskIn(date, tasks, newExemplar)
        print('at sec',type(tasks))
        print(tasks)
        if tasks != None:
            #iterable_tasks = iter(tasks)
            #next(iterable_tasks,None)
            i = 0
            #for task in iterable_tasks:
            for j in range(len(tasks)):
                print('ura')
                container.create_1(i, date)
                i += 1
        if date:
            self.ui.current_date.setText(f'<html><head/><body><p align="center"><span style=" font-size:36pt;">{str(date)}</span></p></body></html>')
        self.ui.verticalLayout.addWidget(container)

        ## Диалоговые кнопки

        dialog_buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,  QtCore.Qt.Horizontal, self)
        dialog_buttons.setLayoutDirection(QtCore.Qt.RightToLeft)
        dialog_buttons.accepted.connect(self.accept)
        dialog_buttons.rejected.connect(self.new_task)
        dialog_buttons.button(QtWidgets.QDialogButtonBox.Cancel).setText("Новая задача")
        dialog_buttons.button(QtWidgets.QDialogButtonBox.Ok).setText("Сохранить")

        self.ui.verticalLayout.addWidget(dialog_buttons)

    def accept(self):
        print('Saved')

    def new_task(self): #Новая задача, а не реджектед
        taskNumber = -1 #информация о том, что желаем создать новую задачу, а не изменить
        self.new_task_window = EditTaskClass(taskNumber, self.newExemplar, self.date)
        self.new_task_window.show()
