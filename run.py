from datetime import date
import ast
import os

import dateanalysis

def dictHandler(someDict, opening = None):
	# т.е. False по умолчанию и если аргумент opening не указан, то происходит
	# упаковка данных массива в словарь, иначе распаковка словаря

	def openingTheTarget():
		openNote = someDict[i1][i2][i3][elemsCounter].note
		openFlag = someDict[i1][i2][i3][elemsCounter].flag
		return [openNote, openFlag]

	def closingTheTarget():
		closeNote = someDict[i1][i2][i3][elemsCounter][0]
		closeFlag = someDict[i1][i2][i3][elemsCounter][1]
		newExemplar = Target(closeNote)
		if newExemplar.flag != closeFlag:
			newExemplar.changeFlag()
		return newExemplar

	dictRewrited = someDict.copy() 
	for i1, j1 in someDict.items():
		for i2, j2 in someDict[i1].items():
			for i3, j3 in someDict[i1][i2].items():
				for elemsCounter in range(len(someDict[i1][i2][i3])):
					if opening:
						dictRewrited[i1][i2][i3][elemsCounter] = openingTheDictionary()
					else: 
						dictRewrited[i1][i2][i3][elemsCounter] = closingTheDictionary()
	return dictRewrited

# файл будет автоматически создан при попытке его открытия
def new_config(name):
	f1 = open(name1,'w')
	f2 = open(name2,'w')
	f1.close()
	f2.close()

# чтение файла с данными пользователя и запись его содержимого в словарь
def dataReading(filename1: str, filename1: str) -> None:
	if os.path.isfilea(filename1) and os.path.isfilea(filename2) and os.path.isfilea(filename3):
		f1 = open(filename1)
		f2 = open(filename2)
		k_str1 = f1.read()
		k_str2 = f2.read()
		calendarDataPrerewrited = ast.literal_eval(k_str1)
		calendarData = dictHandler(calendarDataPrerewrited)
		notifications = ast.literal_eval(k_str2)
		for i in range(4):
			if notifications[i] != None:
				dateOfLastAnswer[i] = notifications[i[1]]
		f1.close()
		f2.close()
	else:
		new_config('config')
		calendarData = {}
		notifications = [None, None, None, None]
		dateOfLastAnswer = [0, 0, 0, 0]

# запись данных пользователя в файл
def dataWriting(filename: str):
		f = open(filename, 'w')
		calendarDataRewrited = dictHandler(calendarData, opening)
		f.write(str(calendarDataRewrited))
		f.close()

# определяет количество дней в месяце (с учетом високосного года)
def daysInMonth(year, month):
	mdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		isYearLeap = True
	else: isYearLeap = False
	daysamt = mdays[month-1]
	if (month == February and isYearLeap):
		daysamt += 1
	return daysamt

# определяет номер предыдущего месяца (с учетом того, что им может оказаться декабрь)
def LastMonth(year, month):
	if (int(month)-1) = 0:
		month = 12
		year = year - 1
	return [year, month]

# проверка на наличие нужной ячейки в структуре
# создание ячейки в случае ее отсутствия
def checkUp(noteDay):
	if calendarData.get(noteDay[:4]) == None:
		calendarData.setdefault(noteDay[:4], {})
	if calendarData[noteDay[:4]].get(noteDay[5:7]) == None:
		calendarData[noteDay[:4]].setdefault(noteDay[5:7], {})
	if calendarData[noteDay[:4]][noteDay[5:7]].get(noteDay[8:]) == None:
		calendarData[noteDay[:4]][noteDay[5:7]].setdefault(noteDay[8:], [])
		calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]].append(0)

def inquery(number):
	noteDay = input("on what day?")
	checkUp(noteDay)
	if number == 1:
		noteText = input("what u want to write in this cell")
		calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]].append(Target(noteText))
	if number == 2:
		numb = int(input("what number of target?"))
		if len(calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]]) >= numb-1:
			calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb].changeFlag()
			if calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb].flag = True:
				calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][0] += 1
			else: calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][0] -= 1
	if number == 3:
		numb = int(input("what number of target?"))
		#наверное можно избавиться от функции edit класса target
		outputText = calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb].note()
		noteText = input("last note: ", outputText)
		if len(calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]]) >= numb:
			calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb] = Target(noteText)
	if number == 4:
		return calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]]
	if (number < 4):
		dataWriting('config')

def questionForUser():
	question = int(input("""what u want from me?
		1 - new target
		2 - watch targets on this day
		3 - edit target
		4 - change status of target
		"""))
	inquery(question)

def printCalendar(): 
	pass

class Target(object):

	__slots__ = ('note', 'flag')

	def __init__(self, text):
		self.note = text
		self.flag = False #по умолчанию создаваемая задача считается невыполненной

	def edit(self):
		self.note = input()#!!! перенести ввод в другое место, а тут уже получать имеющиеся данные
		#необходимо сделать, чтобы это поле оставалось заполненным предыдущими данными в момент редактирования

	def changeFlag(self):
		self.flag = not self.flag

if __name__ == '__main__':

	dataReading('config')

	todaysDate = date.today()
	daysInThisMonth = 0
	yearNumber = str(todaysDate)[:4]
	monthNumber = str(todaysDate)[5:7]
	dayNumder = str(todaysDate)[8:]
	order = date(int(yearNumber), int(monthNumber), 1).weekday()
	daysInThisMonth = daysInMonth(yearNumber, monthNumber)

	printCalendar()
	questionForUser()

	exit = False
	while not exit1:
		dateanalysisWorkResults = dateanalysis.Notification(todaysDate, calendarData,
			daysInMonth(LastMonth(yearNumber, monthNumber)[0], LastMonth(yearNumber, monthNumber)[1]))
		while not exit2:
			dateanalysisWorkResults = dateanalysis.controller()
			if dateanalysisWorkResults != None:
				notifications.append(dateanalysisWorkResults)
				dateOfLastAnswer[dateanalysisWorkResults[1]] = dateanalysisWorkResults[2]
		exit1 = True
