import os
import ast
import datetime
from datetime import date



# чтение файла с данными пользователя и запись его содержимого в словарь
def dataReading(filename: str):
	if os.path.isfile(filename):
		f = open(filename)
		k_str = f.read()
		k_array = ast.literal_eval(k_str)
		tasksDict = k_array[0]
		usersGrades = k_array[1]
		notifications = k_array[2]
		for i in range(4):
			if notifications[i] != None:
				dateOfLastAnswer[i] = notifications[i][1]
			else: 
				dateOfLastAnswer[i] = None
		f.close()
		return [tasksDict, usersGrades, notifications, dateOfLastAnswer]
	else:
		return questionToTheUsersAssessment()

# запись данных пользователя в файл
# формат: tasksDict, usersGrades, notifications
def dataWriting(filename: str, setOfThree: list) -> None:
	# даже при первом запуске файл будет автоматически создан при попытке его открытия
	f = open(filename, 'w')
	f.write(str(setOfThree))
	f.close()



class Meave(object):

	__slots__ = ('tasksDict', 'usersGrades', 'notifications')

	def __init__(self, data: dict, grades: dict, notific: dict) -> None:
		self.tasksDict = data
		self.usersGrades = grades
		self.notifications = notific

	# проверка на наличие нужной ячейки в структуре
	# создание ячейки в случае ее отсутствия
	def checkUp(self, date: datetime.datetime) -> list:
		y, m, d = date.year, date.month, date.day
		if self.tasksDict.get(y) == None:
			self.tasksDict.setdefault(y, {})
		if self.tasksDict[y].get(m) == None:
			self.tasksDict[y].setdefault(m, {})
		if self.tasksDict[y][m].get(d) == None:
			self.tasksDict[y][m].setdefault(d, {})
			self.tasksDict[y][m][d].setdefault('totalGrades', {})
			self.tasksDict[y][m][d]['totalGrades'].setdefault('completed', 0)
			self.tasksDict[y][m][d]['totalGrades'].setdefault('all', 0)
			self.tasksDict[y][m][d].setdefault('allEvents', [])
		return self.tasksDict[y][m][d]
		#dataWriting('config', [self.tasksDict, self.usersGrades, self.notifications])

	def newTask(self, note: str, grade: int, date: datetime.datetime) -> None:
		tDict = self.checkUp(date)
		tDict['totalGrades']['all'] += grade
		tDict['allEvents'].append({'note': note, 'grade': grade, 'flag': False})
		dataWriting('config', [self.tasksDict, self.usersGrades, self.notifications])

	def deleteTask(self, date: datetime.datetime, number: int) -> None:
		tDict = self.checkUp(date)
		if len(tDict['allEvents']) > number and number >= 0:
			if tDict['allEvents'][number]['flag']:
				tDict['totalGrades']['completed'] -= tDict['allEvents'][number]['grade']
			tDict['totalGrades']['all'] -= tDict['allEvents'][number]['grade']
			tDict['allEvents'].pop(number)
			dataWriting('config', [self.tasksDict, self.usersGrades, self.notifications])

	def changeFlag(self, date: datetime.datetime, number: int) -> None:
		tDict = self.checkUp(date)
		if len(tDict['allEvents']) > number and number >= 0:
			#если задание было помечено как выполненное, то вычесть баллы этого задания
			if tDict['allEvents'][number]['flag']:
				tDict['allEvents'][number]['flag'] = False
				tDict['totalGrades']['completed'] -= tDict['allEvents'][number]['grade']
			else:
			#иначе прибавить
				tDict['allEvents'][number]['flag'] = True
				tDict['totalGrades']['completed'] += tDict['allEvents'][number]['grade']
			dataWriting('config', [self.tasksDict, self.usersGrades, self.notifications])

	def changeTask(self, number: int, noteText: str, noteGrade: int, noteFlag: bool, date: datetime.datetime) -> None:
		tDict = self.checkUp(date)
		if len(tDict['allEvents']) > number and number >= 0:
			noteFlag = tDict['allEvents'][number]['flag']
			tDict['totalGrades']['all'] -= tDict['allEvents'][number]['grade']
			if tDict['allEvents'][number]['flag']:
				tDict['totalGrades']['completed'] -= tDict['allEvents'][number]['grade']
			tDict['allEvents'][number] = {'note': noteText, 'grade': noteGrade, 'flag': noteFlag}
			tDict['totalGrades']['all'] += tDict['allEvents'][number]['grade']
			if tDict['allEvents'][number]['flag']:
				tDict['totalGrades']['completed'] += tDict['allEvents'][number]['grade']
			dataWriting('config', [self.tasksDict, self.usersGrades, self.notifications])

	def getTasksOfday(self, date: datetime.datetime) -> list:
		tDict = self.checkUp(date)
		return tDict['allEvents']

	def daysInMonth(self, year, month) -> int:
		mdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		daysamt = mdays[int(month)-1]
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			if month == 2:
				daysamt += 1
		return daysamt

	def dayColor(self, date) -> int:
		tDict = self.checkUp(date)
		if tDict['totalGrades']['all'] != 0:
			ratio = tDict['totalGrades']['completed'] / tDict['totalGrades']['all']
			return {
				ratio <= self.usersGrades[0] : Qt.QColor(244,156,59),
				self.usersGrades[0] <= ratio < self.usersGrades[1] : Qt.QColor(242,59,27),
				self.usersGrades[1] <= ratio < self.usersGrades[2] : Qt.QColor(197,14,78),
				self.usersGrades[2] <= ratio : Qt.QColor(143,11,113)
			}[True]
		else: return Qt.QColor(244,156,59)


		
if __name__ == '__main__':
	tasksDict = {}
	usersGrades = []
	notifications = [None, None, None, None]
	dateOfLastAnswer = notifications
	if os.path.isfile('config'):
		tasksDict, usersGrades, notifications, dateOfLastAnswer = dataReading('config')
	newExemplar = Meave(tasksDict, usersGrades, notifications)

	from PyQt5 import Qt, QtCore, QtWidgets
	import qt, sys, qss

	app = Qt.QApplication(sys.argv)
	app.setStyleSheet(qss.BLACK_STACKOVERFLOW)
	window = qt.LoadScreen(newExemplar)
	window.show()
	sys.exit(app.exec_())
	