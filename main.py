import os
import ast
import datetime
from datetime import date



def questionToTheUsersAssessment():
	print("""
		Предположим, вы поставили себе 10 равнозначных задач.
		Какое количество из них вам бы достаточно было выполнить...
		""")
	usersGrades.append(int(input("чтобы показать удовлетворительный результат?"))/10)
	usersGrades.append(int(input("чтобы показать хороший результат?"))/10)
	usersGrades.append(int(input("чтобы показать отличный результат?"))/10)
	#dataWriting('usersGradesConfig', '3')
	return usersGrades

# чтение файла с данными пользователя и запись его содержимого в словарь
def dataReading(filename: str):
	if os.path.isfile(filename):
		f = open(filename)
		k_str = f.read()
		k_array = ast.literal_eval(k_str)
		calendarData = k_array[0]
		usersGrades = k_array[1]
		notifications = k_array[2] lepLEP96
		for i in range(4):
			if notifications[i] != None:
				dateOfLastAnswer[i] = notifications[i][1]
			else: 
				dateOfLastAnswer[i] = None
		f.close()
		return [calendarData, usersGrades, notifications, dateOfLastAnswer]
	else:
		return questionToTheUsersAssessment()

def dataCheck(filename: str):
	if os.path.isfile(filename):
		dataReading(filename)
		return True

# запись данных пользователя в файл
# формат: calendarData, usersGrades, notifications
def dataWriting(filename: str, setOfThree: list) -> None:
	# даже при первом запуске файл будет автоматически создан при попытке его открытия
	f = open(filename, 'w')
	f.write(str(setOfThree))
	f.close()



class Meave(object):

	__slots__ = ('calendarData', 'usersGrades', 'notifications')

	def __init__(self, data: dict, grades: dict, notific: dict) -> None:
		self.calendarData = data
		self.usersGrades = grades
		self.notifications = notific

	# проверка на наличие нужной ячейки в структуре
	# создание ячейки в случае ее отсутствия
	def checkUp(self, y, m, d) -> list:
		if self.calendarData.get(y) == None:
			self.calendarData.setdefault(y, {})
		if self.calendarData[y].get(m) == None:
			self.calendarData[y].setdefault(m, {})
		if self.calendarData[y][m].get(d) == None:
			self.calendarData[y][m].setdefault(d, {})
			self.calendarData[y][m][d].setdefault('totalGrades', {})
			self.calendarData[y][m][d]['totalGrades'].setdefault('completed', 0)
			self.calendarData[y][m][d]['totalGrades'].setdefault('all', 0)
			self.calendarData[y][m][d].setdefault('allEvents', [])
		#dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def dateConversion(self, date: datetime.datetime) -> list:
		y, m, d = date.year, date.month, date.day
		self.checkUp(y, m, d)
		return self.calendarData[y][m][d]

	def newTask(self, note: str, grade: int, date: datetime.datetime) -> None:
		cData = self.dateConversion(date)
		cData['totalGrades']['all'] += grade
		cData['allEvents'].append({'note': note, 'grade': grade, 'flag': False})
		dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def deleteTask(self, date: datetime.datetime, number: int) -> None:
		cData = self.dateConversion(date)
		if len(cData['allEvents']) > number and number >= 0:
			if cData['allEvents'][number]['flag']:
				cData['totalGrades']['completed'] -= cData['allEvents'][number]['grade']
			cData['totalGrades']['all'] -= cData['allEvents'][number]['grade']
			cData['allEvents'].pop(number)
			dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def changeFlag(self, date: datetime.datetime, number: int) -> None:
		cData = self.dateConversion(date)
		if len(cData['allEvents']) > number and number >= 0:
			#если задание было помечено как выполненное, то вычесть баллы этого задания
			if cData['allEvents'][number]['flag']:
				cData['allEvents'][number]['flag'] = False
				cData['totalGrades']['completed'] -= cData['allEvents'][number]['grade']
			else:
			#иначе прибавить
				cData['allEvents'][number]['flag'] = True
				cData['totalGrades']['completed'] += cData['allEvents'][number]['grade']
			dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def changeTask(self, date: datetime.datetime, number: int) -> None:
		cData = self.dateConversion(date)
		if len(cData['allEvents']) > number and number >= 0:
			outputText1 = cData['allEvents'][number]['note']
			outputText2 = cData['allEvents'][number]['grade']
			print("last note: ", outputText1)
			noteText = input("new note: ")
			print("last grade: ", outputText2)
			noteGrade = int(input("new grade: "))
			noteFlag = cData['allEvents'][number]['flag']
			cData['totalGrades']['all'] -= cData['allEvents'][number]['grade']
			if cData['allEvents'][number]['flag']:
				cData['totalGrades']['completed'] -= cData['allEvents'][number]['grade']
			cData['allEvents'][number] = {'note': noteText, 'grade': noteGrade, 'flag': noteFlag}
			cData['totalGrades']['all'] += cData['allEvents'][number]['grade']
			if cData['allEvents'][number]['flag']:
				cData['totalGrades']['completed'] += cData['allEvents'][number]['grade']
			dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def getTasksOfday(self, date: datetime.datetime) -> list:
		cData = self.dateConversion(date)
		return cData['allEvents']


		
if __name__ == '__main__':
	calendarData = {}
	usersGrades = []
	notifications = [None, None, None, None]
	dateOfLastAnswer = notifications
	if os.path.isfile('config'):
		calendarData, usersGrades, notifications, dateOfLastAnswer = dataReading('config')
		#date = date.today()
		#calendarData = checkUp(today,calendarData)
		#funcs.analyse(today,calendarData,usersGrades, dateOfLastAnswer,notifications)
	else:
		usersGrades = questionToTheUsersAssessment()
	newExemplar = Meave(calendarData, usersGrades, notifications)