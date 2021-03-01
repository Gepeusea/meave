import datetime

now = datetime.datetime.now()
todaysDate = str(dateime.date.today())

def pushFunction(text):
	return(text)

flag1 == False
flag2 == False
flag3 == False
flag4 == False

def flagController():
	pass

#выводит напоминание, если пользователь сегодня не выполнил ни одного задания
def unproductiveDay(calendarData):
	check = True
	if int(now.hour) == 20 and flag1 == False:
		if calendarData[todaysDate[:4]][todaysDate[5:7]][todaysDate[8:]][0] > 0:
			check = False
		if check:
			pushFunction('Сегодня вы не выполнили ни одной задачи, но еще не поздно это изменить')
		flag1 == True

def calculations(calendarData,daysInLastMonth,counter, returnLen = None):
	attempt = int(todaysDate[8:])-counter
	if attempt < 1:
		attempt = daysInLastMonth + attempt
	attempt = calendarData[todaysDate[:4]][todaysDate[5:7]][str(attempt)]
	elif attempt < 10:
		attempt = calendarData[todaysDate[:4]][todaysDate[5:7]]['0'+str(attempt)]
	if returnLen:
		return len(attempt)
	else: return attempt[0]

#выводит напоминание в случае, если всю последнюю неделю пользователь был непродуктивен
def unproductiveWeek(calendarData,daysInLastMonth):
	check = True
	if int(now.hour) == 12 and flag2 == False:
		for i in range(7):
			if calculations(calendarData,daysInLastMonth,i) > 3:
				check = False
		if check:
			pushFunction('На этой неделе у вас наблюдалась низкая продуктивность, давайте исправим это сегодня')
		flag2 == True

#выводит напоминание когда пользователь поддерживает высокую продуктивность в течение долгого периода
def hightActivity(calendarData,daysInLastMonth):
	check = True
	if int(now.hour) == 12 and flag2 == False:
		for i in range(7):
			if calculations((calendarData,daysInLastMonth,i)+1) < 4:
				check = False
		if check:
			pushFunction('Последнюю неделю вы предерживались режима высокой продуктивности. Что думаете на счет разгрузочного дня?')
		flag2 == True

#напоминание о невыполненных задачах
def outstandingTask(calendarData,daysInLastMonth):
	check = False
	if int(now.hour) == 10 and flag2 == False:
		if calculations(calendarData,daysInLastMonth,1) < (calendarData,daysInLastMonth,1, True)
		pushFunction('У вас есть невыполненные задачи за прошлый день, но вы можете расправиться с ними сегодня')
