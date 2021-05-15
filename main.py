import datetime
from datetime import date

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

	def dateConversion(self, date: datetime.datetime) -> list:
		y, m, d = date.year, date.month, date.day
		self.checkUp(y, m, d)
		return self.calendarData[y][m][d]

	def newTask(self, note: str, grade: int, date: datetime.datetime) -> None:
		cData = self.dateConversion(date)
		cData[0][1] += grade
		cData[1].append([note, grade, False])

	def deleteTask(self, date: datetime.datetime, number: int) -> None:
		cData = self.dateConversion(date)
		if len(cData[1]) > number and number >= 0:
			if cData[1][number][2]:
				cData[0][0] -= cData[1][number][1]
			cData[0][1] -= cData[1][number][1]
			cData[1].pop(number)

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

	def getTasksOfday(self, date: datetime.datetime) -> list:
		cData = self.dateConversion(date)
		return cData[1]
		
if __name__ == '__main__':
	calendarData = {}
	newExemplar = Meave(calendarData)