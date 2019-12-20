# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
import pymysql
import random
import time
from urllib.request import urlopen, Request
import urllib
from bs4 import BeautifulSoup
import ssl

def tupleConvertList(rows):
	results = []
	for elem in rows:
		tmp = []
		for entity in elem:
			tmp.append(entity)
		results.append(tmp)
	return results

def recommendModule(rows, location, age, userTime, intimacy):
	maxPoints = 0
	targetRow = []
	#print(rows)
	targetTime = None
	random.shuffle(rows)
	for elem in rows:
		point = 0
		weekDic = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}
		weekDay = int(time.localtime(time.time()).tm_wday)
		if userTime == 'now' : targetTime = int(time.localtime(time.time()).tm_hour)
		elif userTime == 'morning' : targetTime = 9
		elif userTime == 'lunch': targetTime = 12
		elif userTime == 'afternoon': targetTime = 14
		elif userTime == 'dinner': targetTime = 18
		elif userTime == 'night': targetTime = 22
		elif userTime == 'dawn': targetTime = 2
		#else: targetTime = 15
		if elem[4] != 'None' or elem[4] != None:
			timeRange = elem[4].split('-')
			startTime = int(timeRange[0])
			endTime = int(timeRange[1])
			if startTime <= targetTime and targetTime < endTime: point += 2
			if len(elem[4])==3 and elem[4] in weekDic:
				if weekDic[elem[4][2]] == weekDay: point -= 10
					#print('point1')
				else: point += 1

		#intimacy
		if elem[3] == intimacy: point += 3

		#weather
		if location == 'north': location = '제주시'
		elif location == 'west': location = '중문동'
		elif location == 'east': location = '조천읍'
		enc_location = urllib.parse.quote(location + '+날씨')
		url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location
		context = ssl._create_unverified_context()
		page = urlopen(url,context=context)
		html = page.read()
		soup = BeautifulSoup(html,"html.parser")
		temperature = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
		rain = soup.find('ul', class_='info_list').find('p', class_='cast_txt').text.split(',')[0]

		if rain == '흐림' or rain == '비':
			if elem[8] == 'out': point -= 10
			else: point += 2

		#print("point ------ = " + str(point))
		#print(elem)
		#point
		if maxPoints < point:
			maxPoints = point
			targetRow = elem

	return targetRow


def recommend_place(location, activity, age, userTime, intimacy):
	db = pymysql.connect(host = 'us-cdbr-iron-east-05.cleardb.net', user = 'be1a9b3ed30fc3', password = '5aff62241de580e', db = 'heroku_2568178937c7ba4', autocommit = True)
	cur = db.cursor()
	db.ping(reconnect=True)
	cur.execute('select * from keywords where activity=' + '"' + activity + '" and location="' + location +'"')
	rows = cur.fetchall()
	db.close()
	rows = tupleConvertList(rows)
	resultPlace = recommendModule(rows, location, age, userTime, intimacy)
	return resultPlace

print(recommend_place('north', 'cafe', '20s', 'afternoon', 'pet'))