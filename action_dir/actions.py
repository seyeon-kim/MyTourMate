# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.events import SlotSet

import pymysql
import random
import time
from urllib.request import urlopen, Request
import urllib
import bs4
from bs4 import BeautifulSoup
import ssl

rows = []
points = []
specials = []
globalActivity = None

def tupleConvertList(rows):
	global points

	results = []
	for elem in rows:
		tmp = []
		for entity in elem:
			tmp.append(entity)
		results.append(tmp)
		points.append(0)
	return results

def recommend():
	global rows
	global points

	resultPlaces = []
	resultPoints = []
	for i in range(len(points)):
		if points[i] > 0:
			resultPlaces.append(rows[i])
			resultPoints.append(points[i])
	#print(resultPlaces)
	points = resultPoints
	return resultPlaces

def recommendPlace(location, needs, activity):
	global rows
	global points

	newRows = []
	newPoints = []
	#print(needs)
	#print(activity)
	#print(rows)
	for i in range(len(rows)):
		elem = rows[i]
		dbAct = elem[1]
		if activity != None and activity != 'None':
			if dbAct == activity:
				newRows.append(elem)
				newPoints.append(points[i]+2)
				points[i] += 2
		else:
			if needs == "rest":
				#print("할렐루야")
				if dbAct == "pub" or dbAct == "cafe":
					points[i] += 2
				elif dbAct == "natural" or dbAct == "historic":
					points[i] += 1
			elif needs == "play":
				if dbAct == "museum" or dbAct =="market" or dbAct=="shopping":
					points[i] += 2
			elif needs == "sightsee":
				if dbAct == "museum" or dbAct == "historic" :
					points[i] += 2
				elif dbAct=="shopping" or dbAct == "market":
					points[i] += 1
			elif needs == "eat":
				if dbAct == "restaurant":
					points[i] += 2
				elif dbAct == "cafe" or dbAct == "pub" or dbAct == "market":
					points[i] += 1
			newRows.append(elem)
			newPoints.append(points[i])

		
		if location == 'north': location = '제주시'
		elif location == 'west': location = '중문동'
		elif location == 'east': location = '조천읍'
		else: location = '제주'
		enc_location = urllib.parse.quote(location + '+날씨')
		url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location
		context = ssl._create_unverified_context()
		page = urlopen(url,context=context)
		html = page.read()
		soup = BeautifulSoup(html,"html.parser")
		temperature = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
		rain = soup.find('ul', class_='info_list').find('p', class_='cast_txt').text.split(',')[0]

		if rain == '흐림' or rain == '비':
			if elem[8] != 'out':
				newRows.append(elem)
				newPoints.append(points[i]+2)
				points[i] += 2
		
	rows = newRows
	points = newPoints
	result = recommend()
	return result




# 나이 db 데이터 세팅 
class ActionSetAge(Action):
	def name(self) -> Text:
		return "action_set_age"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		print("[DEBUG] set age Complete")
		return []

def findKeywords(keywords):
	global rows
	global points

	newRows = []
	newPoints = []
	duplicate = []

	for i in range(len(rows)):
		row = rows[i]
		for keyword in keywords:
			if keyword in row[5] and rows[0] not in duplicate:
				newRows.append(row)
				duplicate.append(row[0])
				newPoints.append(points[i] + 2)
				break

	rows = newRows
	points = newPoints
	print("-----------find keywords----------")
	print(rows)
	print("----------------------------------")
	return

#여기서 DB 불러옴
class ActionSetLocation(Action):
	def name(self) -> Text:
		return "action_set_location"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		global rows
		global globalActivity
		global specials
		location = tracker.get_slot('location')
		db = pymysql.connect(host = 'us-cdbr-iron-east-05.cleardb.net', user = 'be1a9b3ed30fc3', password = '5aff62241de580e', db = 'heroku_2568178937c7ba4', autocommit = True)
		cur = db.cursor()
		db.ping(reconnect=True)
		if globalActivity == None:
			cur.execute('select * from keywords where location="' + location +'"')
		else:
			cur.execute('select * from keywords where location="' + location +'"and activity="' + globalActivity + '"')
		rows = cur.fetchall()
		db.close()
		rows = tupleConvertList(rows)
		if specials != []:
			findKeywords(specials)
		print(rows)
		print("[DEBUG] location 세팅")
		#dispatcher.utter_message("로케이션 세팅 완료!")
		return []


class ActionSetSpecial(Action):
	def name(self) -> Text:
		return "action_set_special"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		global specials

		special = tracker.get_slot('special')
		if special == None or special == 'None': return []
		if special == "insta" or special == "인스타" : specials = ["인스타", "감성"]
		elif special == "dessert": specials = ["디저트", "케이크", "타르트", "마카롱", "다쿠아", "에그타르트"]
		elif special == "photo": specials = ["사진", "스팟", "포토", "전경", "바다"]
		elif special == "view": specials = ["전경", "바다", "뷰", "경치"]
		elif special == "gift": specials = ["선물", "시장", "플리마켓"]
		elif special == "mood": specials = ["인테리어", "감성", "인스타"]
		elif special == "local" or special == "도민": specials = ["로컬", "도민"]
		else: specials.append(special)
		
		print("[DEBUG] special 세팅 완료: " + special)
		return []

class ActionSetActivity(Action):
	def name(self) -> Text:
		return "action_set_activity"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		global globalActivity
		activity = tracker.get_slot('activity')
		if activity != None: globalActivity = activity
		print("[DEBUG] activity 세팅: globalActivity")
		#dispatcher.utter_message("로케이션 세팅 완료!")
		return []

class ActionSetIntimacy(Action):
	def name(self) -> Text:
		return "action_set_intimacy"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		global rows
		global points
		intimacy = tracker.get_slot('intimacy')

		for i in range(len(rows)):
			if rows[i][3] == intimacy:
				points[i] += 3
		print("[DEBUG] set intimacy Complete:" + intimacy)
		return []

def checkUserTime(userTime):
	if userTime == 'now' : 
		return int(time.localtime(time.time()).tm_hour)
	elif userTime == 'morning' : return 9
	elif userTime == 'lunch': return 12
	elif userTime == 'afternoon' or userTime == "noon": return 14
	elif userTime == 'dinner': return 18
	elif userTime == 'night': return 22
	elif userTime == 'dawn': return 2
	else: return 15

class ActionSetTime(Action):
	def name(self) -> Text:
		return "action_set_time"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		global rows
		global points
		newRows = []
		newPoints = []

		userTime = tracker.get_slot('time')
		if userTime == None or userTime == 'None': return []
		# 오늘은 무슨 요일인지 알아내기
		weekDic = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}
		weekDay = int(time.localtime(time.time()).tm_wday)
		targetTime = checkUserTime(userTime)
		# Time에 대한 점수 환산

		for i in range(len(rows)):
			dbTime = rows[i][4]
			if (dbTime != 'None' or dbTime != None) and '-' in dbTime:
				timeRange = dbTime.split('-')
				print(timeRange)
				if timeRange != ['None']:
					startTime = int(timeRange[0])
					endTime = int(timeRange[1])
					if len(dbTime) == 3 and dbTime in weekDic:
						if weekDic[dbTime[2]] == weekDay: pass
						else: 
							newRows.append(rows[i])
							newPoints.append(points[i]+1)
							points[i] += 1

					if startTime <= targetTime and targetTime < endTime: 
						print(startTime)
						print(endTime)
						print(targetTime)
						newRows.append(rows[i])
						newPoints.append(points[i]+2)
						points[i] += 2
				else:
					newRows.append(rows[i])
					newPoints.append(points[i])
			else:
				newRows.append(rows[i])
				newPoints.append(points[i])

		rows = newRows
		points = newPoints
		print("[DEBUG] set Time Complete")
		return []



def resultMessegeUnit(resultPlace):
	title = resultPlace[0]
	subtitle = resultPlace[5]
	imgUrl = str(resultPlace[6])
	urlInfo = resultPlace[7]
	if urlInfo == None or urlInfo == 'None' : urlInfo = "https://www.google.com/search?q=" + title
	message = {}
	message = {
		"title": title,
		"image_url": imgUrl,
		"subtitle": subtitle + "곳이에요!",
		"default_action": {
			"type": "web_url",
			"url": urlInfo,
			"webview_height_ratio": "tall",
		},
		"buttons": [
			{
				"type": "web_url",
				"url": urlInfo,
				"title": "자세히 알아보기"
			},
			{
				"type": "postback",
				"title": "좋아",
				"payload": "DEVELOPER_DEFINED_PAYLOAD"
			}
		]
		}

	return message

def convertNeeds(needs):
	if needs == None or needs == 'None': return None

	if needs in ['rest', 'play', 'sightsee', 'eat']: return needs
	if '쉬' in needs or '쉴' in needs : return 'rest'
	elif '노' in needs or '놀' in needs : return 'play'
	elif '보' in needs or '볼' in needs : return 'sightsee'
	elif '머' in needs or '먹' in needs : return 'eat'
	else: return 'rest'


def ranking(resultplaces):
	global points
	newPoints = []
	for i in range(len(points)):
		newPoints.append([i, points[i]])

	newPoints = sorted(newPoints, key= lambda point:point[1], reverse=True)
	newResults = []
	for i in range(5):
		newResults.append(resultplaces[newPoints[i][0]])
	return newResults

class ActionRecomPlace(Action):
	def name(self) -> Text:
		return 'action_recom_place'
		
	def run(self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		act = tracker.get_slot('activity')
		needs = convertNeeds(tracker.get_slot('needs'))
		#print(needs)

		age = tracker.get_slot('age')
		location = tracker.get_slot('location')

		# 미성년자 방지
		if age == '10s' and act == 'pub': act = 'cafe'

		message= {}
		resultPlaces = recommendPlace(location, needs, act)
		#resultPlace = ['브와두스','cafe','north',None,'09-23','제주 수제 타르트와 케이크 맛집으로 유명한','https://i.imgur.com/TrEHjNb.png','https://www.instagram.com/voixdoucebakery/','in']

		if resultPlaces != []:
			
			if len(resultPlaces) > 5:
				resultPlaces = ranking(resultPlaces)

			elements = []
			for place in resultPlaces:
				#print(place)
				elements.append(resultMessegeUnit(place))

			message = {
				"attachment": {
					"type": "template",
					"payload": {
						"template_type": "generic",
						"elements": elements
					}
				}
			}
			dispatcher.utter_message("다음을 추천해요.")
			dispatcher.utter_message("말씀주신 원하는 시간에 오늘 방문가능하고, 주신 정보와 날씨도 고려해서 추천한 데이터입니다 :)")
			dispatcher.utter_custom_json(message)
			print("추천완료")
		else:
			dispatcher.utter_message("조금 더 정보를 모아올께요!")
			print("추천실패")
		
		return []






