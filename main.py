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
	return [False, usersGrades]

# чтение файла с данными пользователя и запись его содержимого в словарь
def dataReading(filename: str) -> None:
	if os.path.isfile(filename):
		f = open(filename)
		k_str = f.read()
		k_array = ast.literal_eval(k_str)
		calendarDataPrerewrited = k_array[0]
		calendarData = k_array[0]
		usersGrades = k_array[1]
		notifications = k_array[2]
		for i in range(4):
			if notifications[i] != None:
				dateOfLastAnswer[i] = notifications[i][1]
			else: 
				dateOfLastAnswer[i] = None
		f.close()
		return [True, [calendarData, usersGrades, notifications, dateOfLastAnswer]]
	else:
		return questionToTheUsersAssessment()

# запись данных пользователя в файл
# формат: calendarData, usersGrades, notifications
def dataWriting(filename: str, setOfThree: list) -> None:
	# даже при первом запуске файл будет автоматически создан при попытке его открытия
	f = open(filename, 'w')
	f.write(str(setOfThree))
	f.close()



class Meave(object):

	__slots__ = ('calendarData')

	def __init__(self, data: dict) -> None:
		self.calendarData = data

	# проверка на наличие нужной ячейки в структуре
	# создание ячейки в случае ее отсутствия
	def checkUp(self, y, m, d) -> list:
		if self.calendarData.get(y) == None:
			self.calendarData.setdefault(y, {})
		if self.calendarData[y].get(m) == None:
			self.calendarData[y].setdefault(m, {})
		if self.calendarData[y][m].get(d) == None:
			self.calendarData[y][m].setdefault(d, [])
			self.calendarData[y][m][d].append([0,0])
			self.calendarData[y][m][d].append([])
		#dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def dateConversion(self, date: datetime.datetime) -> list:
		y, m, d = date.year, date.month, date.day
		self.checkUp(y, m, d)
		return self.calendarData[y][m][d]

	def newTask(self, note: str, grade: int, date: datetime.datetime) -> None:
		cData = self.dateConversion(date)
		cData[0][1] += grade
		cData[1].append([note, grade, False])
		dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def deleteTask(self, date: datetime.datetime, number: int) -> None:
		cData = self.dateConversion(date)
		if len(cData[1]) > number and number >= 0:
			if cData[1][number][2]:
				cData[0][0] -= cData[1][number][1]
			cData[0][1] -= cData[1][number][1]
			cData[1].pop(number)
			dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def changeFlag(self, date: datetime.datetime, number: int) -> None:
		cData = self.dateConversion(date)
		if len(cData[1]) > number and number >= 0:
			#если задание было помечено как выполненное, то вычесть баллы этого задания
			if cData[1][number][2]:
				cData[1][number][2] = False
				cData[0][0] -= cData[1][number][1]
			else:
			#иначе прибавить
				cData[1][number][2] = True
				cData[0][0] += cData[1][number][1]
			dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def changeTask(self, date: datetime.datetime, number: int) -> None:
		cData = self.dateConversion(date)
		if len(cData[1]) > number and number >= 0:
			outputText1 = cData[1][number][0]
			outputText2 = cData[1][number][1]
			print("last note: ", outputText1)
			noteText = input("new note: ")
			print("last grade: ", outputText2)
			noteGrade = int(input("new grade: "))
			noteFlag = cData[1][number][2]
			cData[0][1] -= cData[1][number][1]
			if cData[1][number][2]:
				cData[0][0] -= cData[1][number][1]
			cData[1][number] = [noteText, noteGrade, noteFlag]
			cData[0][1] += cData[1][number][1]
			if cData[1][number][2]:
				cData[0][0] += cData[1][number][1]
			dataWriting('config', [self.calendarData, self.usersGrades, self.notifications])

	def getTasksOfday(self, date: datetime.datetime) -> list:
		cData = self.dateConversion(date)
		return cData[1]


		
if __name__ == '__main__':
	calendarData = {}
	usersGrades = []
	notifications = [None, None, None, None]
	dateOfLastAnswer = notifications
	rezult = dataReading('config')
	if rezult[0]:
		calendarData, usersGrades, notifications, dateOfLastAnswer = rezult[1]
		#calendarData = checkupfunc.checkUp(today,calendarData)
		#funcs.analyse(today,calendarData,usersGrades, dateOfLastAnswer,notifications)
	else:
		usersGrades = rezult[1]
	newExemplar = Meave(calendarData)