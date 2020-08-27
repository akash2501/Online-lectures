import webbrowser,time
import xlrd
import pandas as pd
from datetime import datetime,date
import calendar
import numpy as np
timetable = pd.read_excel('C:\\Users\\Akash\\Desktop\\class\\timetable.xlsx')

link = pd.read_excel('C:\\Users\\Akash\\Desktop\\class\\link.xlsx')
link = link.set_index('Staff')
link = link.drop(columns=['Sr. No.', 'Subjects'])
currentday = date.today().strftime('%A')
timetable = timetable.loc[timetable['Day']==currentday]
timetable = timetable.set_index('Day')
timetable = timetable.astype(object).replace(np.nan, 'no')
y = link.to_dict()
now = datetime.now()
while True:
	if now < now.replace(hour=18, minute=0, second=0, microsecond=0) and now >= now.replace(hour=17, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,9,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now < now.replace(hour=17, minute=0, second=0, microsecond=0) and now >= now.replace(hour=16, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,8,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now < now.replace(hour=16, minute=0, second=0, microsecond=0) and now >= now.replace(hour=15, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,7,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now < now.replace(hour=15, minute=0, second=0, microsecond=0) and now >= now.replace(hour=14, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,6,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
		break
	elif now < now.replace(hour=14, minute=0, second=0, microsecond=0) and now >= now.replace(hour=13, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,5,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now < now.replace(hour=13, minute=0, second=0, microsecond=0) and now >= now.replace(hour=12, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,4,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now < now.replace(hour=12, minute=0, second=0, microsecond=0) and now >= now.replace(hour=11, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,3,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now < now.replace(hour=11, minute=0, second=0, microsecond=0) and now >= now.replace(hour=10, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,2,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now < now.replace(hour=10, minute=0, second=0, microsecond=0):
		teacher = timetable.get_value(0,1,takeable=True)
		if teacher == 'no':
			break
		else:
			url = y['Link'][teacher]
			webbrowser.register('chrome',
				None,
			webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
			webbrowser.get('chrome').open(url)
			break
	elif now.hour >= 18:
		print('no classes come tommorrow')
	else:
		break





