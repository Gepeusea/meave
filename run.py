from datetime import date
import ast

#НЕ ЧИТАЙТЕ МОЙ КОД ПОЖАВСТА ОН НЕ ДОПИСАН <3
f = open('config')
k_str = f.read()
calendarData = ast.literal_eval(k_str)
#сделать проверку на существование файла 
#и его создание, в случае, когда проверка не пройдена

#при создании файла стоит не забывать, что если это пустой файл
#без расширения, то стоит ожиджать ошибки
#SyntaxError: unexpected EOF while parsing при попытке чтения

mdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#correct date filling is 2021-02-28
todaysDate = date.today()
daysInThisMonth = 0
yearNumber = str(todaysDate)[:4]
monthNumber = str(todaysDate)[5:7]
dayNumder = str(todaysDate)[8:] 
order = date(int(yearNumber), int(monthNumber), 1).weekday()

def daysInMonth(year, month):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		isYearLeap = True
	else: isYearLeap = False
	daysamt = mdays[month-1]
	if (month == February and isYearLeap):
		daysamt += 1
	return daysamt

def checkUp(noteDay):
	if calendarData.get(noteDay[:4]) == None:
		calendarData.setdefault(noteDay[:4], {})
	if calendarData[noteDay[:4]].get(noteDay[5:7]) == None:
		calendarData[noteDay[:4]].setdefault(noteDay[5:7], {})
	if calendarData[noteDay[:4]][noteDay[5:7]].get(noteDay[8:]) == None:
		calendarData[noteDay[:4]][noteDay[5:7]].setdefault(noteDay[8:], [])

def inquery(number):
	noteDay = input("on what day?")
	checkUp(noteDay)
	if number == 1:
		noteText = input("what u want to write in this cell")
		calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]].append(Target(noteText))
		#calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb-1].dataWriting()
	if number == 2:
		return calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]]
	if number == 3:
		numb = int(input("what number of target?"))
		#наверное можно избавиться от функции edit класса target
		outputText = calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb-1].note()
		noteText = input("last note: ", outputText)
		if len(calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]]) >= numb-1:
			calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb-1] = Target(noteText)
	if number == 4:
		numb = int(input("what number of target?"))
		if len(calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]]) >= numb-1:
			calendarData[noteDay[:4]][noteDay[5:7]][noteDay[8:]][numb-1].changeFlag()

question = int(input("""what u want from me?
		1 - new target
		2 - watch targets on this day
		3 - edit target
		4 - change status of target
		"""))

def ConcretDayDate(ThatDay):
	s = str(todaysDate)[:8] + str(ThatDay)
	return s

def printCalendar(): 
	return None

class Target:

	__slots__ = ('note', 'flag')

	def __init__(self, text):
		self.note = text
		self.flag = False #по умолчанию создаваемая задача считается невыполненной

	def dataWriting(self):
		f = open('config', 'w')
		f.write(str(calendarData))
		f.close()

	def edit(self):
		self.note = input()#!!! перенести ввод в другое место, а тут уже получать имеющиеся данные
		#необходимо сделать, чтобы это поле оставалось заполненным предыдущими данными в момент редактирования

	def changeFlag(self):
		self.flag = not self.flag


if __name__ == '__main__':
	printCalendar()
	inquery(question)
	daysInThisMonth = daysInMonth(yearNumber, monthNumber)