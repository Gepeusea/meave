import datetime

def pushFunction(text):
	return([text, todaysDate, now.hour])        
        
def flagController(calendarData, daysInLastMonth, firstStart = None):
        if firstStart:
                global flag1, flag2, flag3, flag4
                flag1 == True
                flag2 == True
                flag3 == True
                flag4 == True
        global now, todaysDate
        now = datetime.datetime.now()
        todaysDate = str(dateime.date.today())

#выводит напоминание, если пользователь сегодня не выполнил ни одного задания
def unproductiveDay(calendarData):
	check = True
	if now.hour == 20 and flag1:
		if calendarData[todaysDate[:4]][todaysDate[5:7]][todaysDate[8:]][0] > 0:
			check = False
		if check:
			pushFunction('Сегодня вы не выполнили ни одной задачи, но еще не поздно это изменить')
			flag1 == False

def calculations(calendarData,daysInLastMonth,counter, returnNumber = None):
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
def unproductiveWeek(calendarData,daysInLastMonth):
	check = True
	if now.hour == 12 and flag2:
		for i in range(7):
			if (calculations(calendarData,daysInLastMonth,i)[0]) > 3:
				check = False
		if check:
			pushFunction('На этой неделе у вас наблюдалась низкая продуктивность, давайте исправим это сегодня')
			flag2 == False

#выводит напоминание когда пользователь поддерживает высокую продуктивность в течение долгого периода
def hightActivity(calendarData,daysInLastMonth):
	check = True
	if now.hour == 12 and flag3:
		for i in range(7):
			if (calculations((calendarData,daysInLastMonth,i)+1)[0]) < 4:
				check = False
		if check:
			pushFunction('Последнюю неделю вы предерживались режима высокой продуктивности. Что думаете на счет разгрузочного дня?')
			flag3 == False

#напоминание о невыполненных задачах
def outstandingTask(calendarData,daysInLastMonth):
	check = False
	if now.hour == 10 and flag4:
		if (calculations(calendarData,daysInLastMonth,1)[0]) < len(calendarData,daysInLastMonth,1, True):
			pushFunction('У вас есть невыполненные задачи за прошлый день, но вы можете расправиться с ними сегодня')
			flag4 == False
