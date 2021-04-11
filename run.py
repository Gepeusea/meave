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
		openGrade = someDict[i1][i2][i3][elemsCounter].grade
		return [openNote, openFlag, openGrade]

	def closingTheTarget():
		closeNote = someDict[i1][i2][i3][elemsCounter][0]
		closeFlag = someDict[i1][i2][i3][elemsCounter][1]
		closeGrade = someDict[i1][i2][i3][elemsCounter][2]
		newExemplar = Target(closeNote, closeGrade)
		if newExemplar.flag != closeFlag:
			newExemplar.changeFlag()
		return newExemplar

	dictRewrited = someDict.copy() 
	for i1, j1 in someDict.items
		for i2, j2 in someDict[i1].items():
			for i3, j3 in someDict[i1][i2].items():
				for elemsCounter in range(len(someDict[i1][i2][i3])):
					if opening:
						dictRewrited[i1][i2][i3][elemsCounter] = openingTheDictionary()
					else: 
						dictRewrited[i1][i2][i3][elemsCounter] = closingTheDictionary()
	return dictRewrited

def questionToTheUsersAssessment():
	print("""
		Предположим, вы поставили себе 10 равнозначных задач.
		Какое количество из них вам бы достаточно было выполнить...
		""")
	usersGrades.append(int(input("чтобы показать удовлетворительный результат?"))/10)
	usersGrades.append(int(input("чтобы показать хороший результат?"))/10)
	usersGrades.append(int(input("чтобы показать отличный результат?"))/10)
	dataWriting('usersGradesConfig', 3)

# чтение файла с данными пользователя и запись его содержимого в словарь
def dataReading(filename1: str, filename2: str, filename3: str) -> None:
	if os.path.isfilea(filename1) and os.path.isfilea(filename2) and os.path.isfilea(filename3):
		f1 = open(filename1)
		f2 = open(filename2)
		f3 = open(filename3)
		k_str1 = f1.read()
		k_str2 = f2.read()
		k_str3 = f3.read()
		calendarDataPrerewrited = ast.literal_eval(k_str1)
		calendarData = dictHandler(calendarDataPrerewrited)
		notifications = ast.literal_eval(k_str2)
		usersGrades = ast.literal_eval(k_str3)
		for i in range(4):
			dateOfLastAnswer[i] = notifications[i[1]]
		f1.close()
		f2.close()
		f3.close()
	else:
		calendarData = {}
		notifications = [None, None, None, None]
		dateOfLastAnswer = notifications
		questionToTheUsersAssessment()

# запись данных пользователя в файл
def dataWriting(filename: str, number):
	# даже при первом запуске ошибки не будет,
	# т.к. файл будет автоматически создан при попытке его открытия
	f = open(filename, 'w')
	if number == 1: 
		calendarDataRewrited = dictHandler(calendarData, opening)
		f.write(str(calendarDataRewrited))
	elif number == 2: f.write(str(notifications))
	elif number == 3: f.write(str(usersGrades))
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
		calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]].append([0,0])

def dayColor(fullDaysDate):
	numberOfTargets = calendarData[fullDaysDate[:4]][fullDaysDate[5:7]][fullDaysDate[8:]][0]
	ratio = numberOfTargets[0] / numberOfTargets[1]
	return {
		ratio <= usersGrades[0] : 0,
		usersGrades[0] <= ratio < usersGrades[1] : 1,
		usersGrades[1] <= ratio < usersGrades[2] : 2,
		usersGrades[2] <= ratio : 3
	}[True]
	# заменить значиния словаря на номера цветов

def printCalendar(chosenDate): 
	daysColors = []
	if ([todaysDate[:4]] in calendarData) and ([todaysDate[5:7]] in calendarData[todaysDate[:4]]):
		for key in calendarData[todaysDate[:4]][todaysDate[5:7]]:
			daysColors.append(dayColor(calendarData[todaysDate[:4]][todaysDate[5:7]][key]))
	return daysColors

def analyse():
	specimenOfDateAnalysis = dateanalysis.Notification(todaysDate, calendarData, usersGrades[1], 
		daysInMonth(LastMonth(yearNumber, monthNumber)[0], LastMonth(yearNumber, monthNumber)[1]))
	for i in range(4):
		dateanalysisWorkResults = exemplarOfDateAnalysis.controller(dateOfLastAnswer)
		if dateanalysisWorkResults != None:
			notifications[dateanalysisWorkResults[1]] = dateanalysisWorkResults
			dateOfLastAnswer[dateanalysisWorkResults[1]] = dateanalysisWorkResults[2]
			dataWriting('notificationsConfig', '2')

def inquery(number):
	noteDay = input("on what day?")
	checkUp(noteDay)
	cData = calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]]
	if number == 1:
		noteText = input("what u want to write in this cell")
		noteGrade = int(input("how difficult is it?"))
		cData.append(Target(noteText, noteGrade))
		cData[0][1] += cData[numb].grade()
	if number == 2:
		numb = int(input("what number of target?"))
		if len(cData) >= numb-1:
			cData[numb].changeFlag()
			if cData[numb].flag = True:
				cData[0] += cData[numb].grade()
			else: cData[0] -= cData[numb].grade()
			daysColors = printCalendar(noteDay)
	if number == 3:
		numb = int(input("what number of target?"))
		#наверное можно избавиться от функции edit класса target
		if len(cData) >= numb:
		outputText1 = cData[numb].note()
		outputText2 = cData[numb].grade()
		noteText = input("last note: ", outputText1)
		noteGrade = input("last grade: ", outputText2)
		noteFlag = cData[numb].flag()
		cData[numb] = Target(noteText, noteGrade)
		cData[numb].flag() = noteFlag
	if number == 4:
		pass
	if number == 5:
		return cData
	if (number < 5):
		dataWriting('dataConfig', '1')

def questionForUser():
	question = int(input("""what u want from me?
		1 - new target
		2 - change status of target
		3 - edit target text
		4 - edit target grade
		5 - watch targets on this day
		"""))
	#watch targets on this day
	#6 - delete target
	inquery(question)

class Target(object):

	__slots__ = ('note', 'flag')

	def __init__(self, text, numeric):
		self.note = text
		self.grade = numeric
		self.flag = False #по умолчанию создаваемая задача считается невыполненной

	def editText(self):
		self.note = input()#!!! перенести ввод в другое место, а тут уже получать имеющиеся данные
		# необходимо сделать, чтобы это поле оставалось заполненным предыдущими данными в момент редактирования

	def editGrade(self):
		self.grade = int(input())#!!! перенести ввод в другое место, а тут уже получать имеющиеся данные

	def changeFlag(self):
		self.flag = not self.flag

if __name__ == '__main__':

	dataReading('dataConfig', 'notificationsConfig', 'usersGradesConfig')

	todaysDate = date.today()
	daysInThisMonth = 0
	yearNumber = str(todaysDate)[:4]
	monthNumber = str(todaysDate)[5:7]
	dayNumder = str(todaysDate)[8:]
	order = date(int(yearNumber), int(monthNumber), 1).weekday()
	daysInThisMonth = daysInMonth(yearNumber, monthNumber)

	analyse()

	daysColors = printCalendar(todaysDate)
	while True:
		questionForUser()
		break
