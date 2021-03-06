import datetime

class Notification:

	def __init__(self, todaysDate, calendarData, daysInLastMonth):
		self.todaysDate = str(todaysDate)
		self.calendarData = calendarData
		self.daysInLastMonth = daysInLastMonth
		self.taskDate1 = self.todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
		self.taskDate2 = self.todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 7, True))
		self.taskDate3 = self.todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 7, True))
		self.taskDate4 = self.todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
		controller()

	def controller(self):
		self.now = datetime.datetime.now()
		notification = unproductiveDay()
		notification = unproductiveWeek()
		notification = hightActivity()
		notification = outstandingTask()
		return notification

	#выводит напоминание, если пользователь сегодня не выполнил ни одного задания
	def unproductiveDay(self):
		check = True
		if (self.now.hour == 20) and (calculations(1, True) == self.taskDate1[8:]):
			if self.calendarData[self.todaysDate[:4]][self.todaysDate[5:7]][self.todaysDate[8:]][0] > 0:
				check = False
			if check:
				self.taskDate1 = self.todaysDate[:8] + str(calculations(1, True))
				return(['Сегодня вы не выполнили ни одной задачи, но еще не поздно это изменить',
					self.todaysDate, self.now.hour])

	def calculations(self, counter, returnNumber = None):
		attempt = int(self.todaysDate[8:])-counter
		if attempt < 1:
			attempt = self.daysInLastMonth + attempt
		if returnNumber:
			return attempt
		attempt = self.calendarData[self.todaysDate[:4]][self.todaysDate[5:7]][str(attempt)]
		elif attempt < 10:
			attempt = self.calendarData[self.todaysDate[:4]][self.todaysDate[5:7]]['0'+str(attempt)]
		return attempt

	#выводит напоминание в случае, если всю последнюю неделю пользователь был непродуктивен
	def unproductiveWeek(daysInLastMonth):
		check = True
		if self.now.hour == 12 and (calculations(7, True) == self.taskDate2[8:]):
			for i in range(7):
				if (calculations(i)[0]) > 3:
					check = False
			if check:
				self.taskDate2 = self.todaysDate[:8] + str(calculations(1, True))
				return(['На этой неделе у вас наблюдалась низкая продуктивность, давайте исправим это сегодня',
					self.todaysDate, self.now.hour])

	#выводит напоминание когда пользователь поддерживает высокую продуктивность в течение долгого периода
	def hightActivity(daysInLastMonth):
		check = True
		if self.now.hour == 12 and (calculations(7, True) == self.taskDate3[8:]):
			for i in range(7):
				if (calculations((i)+1)[0]) < 4:
					check = False
			if check:
				self.taskDate3 = self.todaysDate[:8] + str(calculations(1, True))
				return(['Последнюю неделю вы предерживались режима высокой продуктивности. Что думаете на счет разгрузочного дня?',
					self.todaysDate, self.now.hour])

	#напоминание о невыполненных задачах
	def outstandingTask(daysInLastMonth):
		if self.now.hour == 10 and (calculations(1, True) == self.taskDate4[8:]):
			if (calculations(1)[0]) < len(calculations(1)):
				self.taskDate4 = self.todaysDate[:8] + str(calculations(1, True))
				return(['У вас есть невыполненные задачи за прошлый день, но вы можете расправиться с ними сегодня',
					self.todaysDate, self.now.hour])
