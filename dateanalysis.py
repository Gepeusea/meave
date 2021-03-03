import datetime

#def pushFunction(text):
#	return([text, todaysDate, now.hour])

def flagController(calendarData, daysInLastMonth, firstStart = None):
	if firstStart:
		global taskDate1, taskDate2, taskDate3, taskDate4
		taskDate1 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
		taskDate2 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 7, True))
		taskDate3 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 7, True))
		taskDate4 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
	global now, todaysDate, calendarData
	now = datetime.datetime.now()
	todaysDate = str(dateime.date.today())
	nofication = unproductiveDay()
	nofication = unproductiveWeek()
	nofication = hightActivity()
	nofication = outstandingTask()
	return nofication

#выводит напоминание, если пользователь сегодня не выполнил ни одного задания
def unproductiveDay():
	check = True
	if (now.hour == 20) and (calculations(calendarData,daysInLastMonth, 1, True) == taskDate1[8:]):
		if calendarData[todaysDate[:4]][todaysDate[5:7]][todaysDate[8:]][0] > 0:
			check = False
		if check:	
			#pushFunction('Сегодня вы не выполнили ни одной задачи, но еще не поздно это изменить')
			taskDate1 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
			return(['Сегодня вы не выполнили ни одной задачи, но еще не поздно это изменить', todaysDate, now.hour])

def calculations(daysInLastMonth,counter, returnNumber = None):
	attempt = int(todaysDate[8:])-counter
	if attempt < 1:
		attempt = daysInLastMonth + attempt
	if returnNumber:
		return attempt
	attempt = calendarData[todaysDate[:4]][todaysDate[5:7]][str(attempt)]
	elif attempt < 10:
		attempt = calendarData[todaysDate[:4]][todaysDate[5:7]]['0'+str(attempt)]
	return attempt

#выводит напоминание в случае, если всю последнюю неделю пользователь был непродуктивен
def unproductiveWeek(daysInLastMonth):
	check = True
	if now.hour == 12 and (calculations(calendarData,daysInLastMonth, 7, True) == taskDate2[8:]):
		for i in range(7):
			if (calculations(calendarData,daysInLastMonth,i)[0]) > 3:
				check = False
		if check:
			#pushFunction('На этой неделе у вас наблюдалась низкая продуктивность, давайте исправим это сегодня')
			taskDate2 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
			return(['На этой неделе у вас наблюдалась низкая продуктивность, давайте исправим это сегодня', todaysDate, now.hour])

#выводит напоминание когда пользователь поддерживает высокую продуктивность в течение долгого периода
def hightActivity(daysInLastMonth):
	check = True
	if now.hour == 12 and (calculations(calendarData,daysInLastMonth, 7, True) == taskDate3[8:]):
		for i in range(7):
			if (calculations((calendarData,daysInLastMonth,i)+1)[0]) < 4:
				check = False
		if check:
			#pushFunction('Последнюю неделю вы предерживались режима высокой продуктивности. Что думаете на счет разгрузочного дня?')
			taskDate3 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
			return(['Последнюю неделю вы предерживались режима высокой продуктивности. Что думаете на счет разгрузочного дня?', todaysDate, now.hour])

#напоминание о невыполненных задачах
def outstandingTask(daysInLastMonth):
		if now.hour == 10 and (calculations(calendarData,daysInLastMonth, 1, True) == taskDate4[8:]):
			if (calculations(calendarData,daysInLastMonth,1)[0]) < len(calendarData,daysInLastMonth,1):
				#pushFunction('У вас есть невыполненные задачи за прошлый день, но вы можете расправиться с ними сегодня')
				taskDate4 = todaysDate[:8] + str(calculations(calendarData,daysInLastMonth, 1, True))
				return(['У вас есть невыполненные задачи за прошлый день, но вы можете расправиться с ними сегодня', todaysDate, now.hour])
