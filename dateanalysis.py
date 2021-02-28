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

def calculations(calendarData,daysInLastMonth,counter):
	attempt = int(todaysDate[8:])-counter
	if attempt < 1:
		attempt = daysInLastMonth + attempt
		return calendarData[todaysDate[:4]][todaysDate[5:7]][str(attempt)][0]
	else:
		if attempt < 10:
			return calendarData[todaysDate[:4]][todaysDate[5:7]]['0'+str(attempt)][0]
		else:
			return calendarData[todaysDate[:4]][todaysDate[5:7]][str(attempt)][0]

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
def hightActivity():
	pass

#напоминание о невыполненных задачах
def outstandingTask():
	pass
