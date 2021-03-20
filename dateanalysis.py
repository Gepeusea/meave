import datetime

class Notification:

	def __init__(self, todaysDate, calendarData, daysInLastMonth):
		self.todaysDate = str(todaysDate)
		self.calendarData = calendarData
		self.daysInLastMonth = daysInLastMonth
		self.taskDate = [None, None, None, None]

	# поочередно вызывает все функции
	# потери значений не будет, т.к. единовременно выполниться условия могут только в одной функции 
	def controller(self, taskDates):
		for i in range(4):
			self.taskDate[i] = taskDates[i]
		self.now = datetime.datetime.now()
		notification = unproductiveDay()
		if notification == None:
			notification = unproductiveWeek()
		if notification == None:
			notification = hightActivity()
		if notification == None:
			notification = outstandingTask()
		return notification

	# выводит напоминание, если пользователь сегодня не выполнил ни одного задания
	def unproductiveDay(self):
		check = True
		if (self.now.hour == 20) and (taskDate1 == None or (calculations(1, True) == self.taskDate[0][8:])):
			if self.calendarData[self.todaysDate[:4]][self.todaysDate[5:7]][self.todaysDate[8:]][0] > 0:
				check = False
			if check:
				self.taskDate1 = self.todaysDate[:8] + str(calculations(1, True))
				return(['Сегодня вы не выполнили ни одной задачи, но еще не поздно это изменить',
					0, self.todaysDate, self.now.hour])

	# вычисляет номер дня, месяца и года неделю назад от текущей даты
	# аргумент returnNumber можно не указывать, если требуется вернуть только номер дня
	# если returnNumber при вызове функции указать как True, то вернется массив заданий
	def calculations(self, counter, returnNumber = None):
		attempt = int(self.todaysDate[8:])-counter
		calcMonth = int(self.todaysDate[5:7])
		calcYear = int(self.todaysDate[:4])
		if attempt < 1:
			attempt = self.daysInLastMonth + attempt
			calcMonth = calcMonth - 1
			if calcMonth == 0:
				calcMonth = 12
				calcYear = calcYear - 1
		if returnNumber:
			return attempt
		attempt = self.calendarData[str(calcYear)][str(calcMonth)][str(attempt)]
		elif attempt < 10:
			attempt = self.calendarData[str(calcYear)][str(calcMonth)]['0'+str(attempt)]
		return attempt

	# выводит напоминание в случае, если всю последнюю неделю пользователь был непродуктивен
	def unproductiveWeek(daysInLastMonth):
		check = True
		if self.now.hour == 12 and (taskDate2 == None or (calculations(7, True) == self.taskDate[1][8:])):
			for i in range(7):
				if (calculations(i)[0]) > 4:
					check = False
			if check:
				self.taskDate2 = self.todaysDate[:8] + str(calculations(1, True))
				return(['На этой неделе у вас наблюдалась низкая продуктивность, давайте исправим это сегодня',
					1, self.todaysDate, self.now.hour])

	# выводит напоминание когда пользователь поддерживает высокую продуктивность в течение долгого периода
	def hightActivity(daysInLastMonth):
		check = True
		if self.now.hour == 12 and (taskDate3 == None or (calculations(7, True) == self.taskDate[2][8:])):
			for i in range(7):
				if (calculations((i)+1)[0]) < 5:
					check = False
			if check:
				self.taskDate3 = self.todaysDate[:8] + str(calculations(1, True))
				return(['Последнюю неделю вы предерживались режима высокой продуктивности. Что думаете на счет разгрузочного дня?',
					2, self.todaysDate, self.now.hour])

	# напоминание о невыполненных задачах
	def outstandingTask(daysInLastMonth):
		if self.now.hour == 10 and (taskDate4 == None or (calculations(1, True) == self.taskDate[3][8:])):
			if (calculations(1)[0]) < len(calculations(1)):
				self.taskDate4 = self.todaysDate[:8] + str(calculations(1, True))
				return(['У вас есть невыполненные задачи за прошлый день, но вы можете расправиться с ними сегодня',
					3, self.todaysDate, self.now.hour])
