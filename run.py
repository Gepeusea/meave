from datetime import date
import ast

f = open('config')
k_str = f.read()
calendarData = ast.literal_eval(k_str)

mdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#correct date filling is 2021-02-28
todaysdate = date.today() 
todaysdatestr = str(date.today())
daysInMonth = 0
yearNumber = todaysdatestr[:4]
monthNumber = todaysdatestr[5:7]
dayNumder = todaysdatestr[8:] 
order = date(int(yearNumber), int(monthNumber), 1).weekday()

def daysInMonth(year, month):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		isYearLeap = True
	else: isYearLeap = False
	daysamt = mdays[month-1]
	if (month == February and isYearLeap):
		daysamt += 1
	return daysamt

def inquery(number):
	if number == 1:
		noteDay = int(input("on what day?"))
		noteText = input("what u want to write in this cell")
		newNote = Target(noteText)
	if number == 2:
		noteDay = int(input("on what day?"))
		return
	if number == 3:
		noteDay = int(input("on what day?"))
		numb = int(input("concretely one plz (number of target)"))
	if number == 4:
		noteDay = int(input("on what day?"))
		if len ...
		numb = int(input("concretely one plz (number of target)"))

question = int(input("""what u want from me?
		1 - new target
		2 - watch targets on this day
		3 - edit target
		4 - change status of target
		"""))

def printCalendar(): 
	pass

class Target:

	__slots__ = ('note', 'flag')

	def __init__(self, text):
		self.note = text
		self.flag = False #по умолчанию создаваемая задача считается невыполненной
		dataWriting()

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
	daysInMonth(yearNumber, monthNumber)