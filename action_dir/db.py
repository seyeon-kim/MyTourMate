import pymysql
import csv

db = pymysql.connect(host = 'db name', user = 'user name', password = 'pw name', db = 'db name', autocommit = True)
cur = db.cursor()

def get_query():
	q = ''
	while True:
		print('> ', end = '')
		p = input()
		if p == '':
			break
		q += p + '\n'
	return q


def make_query(csvfilename):
	print('hello')
	f = open(csvfilename + '.csv', 'r', encoding='utf-8', newline='')
	rdr = csv.reader(f)
	entityList = []
	for line in rdr:
		if line[0] == 'name': pass
		print(line)
		newline = []
		for i in range(9):
			wrd = line[i]
			if wrd == '': 
				newline.append("'None'")
			else:
				newline.append("'" + wrd + "'")
		entityList.append(newline)
		print(len(newline))
	f.close()
	return entityList[1:]



class Table:
	def __init__(self, tablename):
		self.tablename = tablename
		self.q = ""

	def tableControl(self):
		if self.q != "":
			try:
				db.ping(reconnect=True)
				cur.execute(self.q)
				rows = cur.fetchall()
				#print(rows)
			except Exception as e:
				print('ERROR({no}): {value}'.format(no = e.args[0], value = e.args[1]))
				#print()
			db.close()


	def createTable(self, entities):
		self.q = "create table " + self.tablename + " (" + entities + ")"
		#for entity in entitylist:
		#	self.q += entity + ", "
		#self.q = self.q[:-2]
		#self.q += ")"
		self.tableControl()

	def insertValue(self, insertValueList):
		self.q = "insert into " + self.tablename + " values ("
		for value in insertValueList:
			self.q += str(value) + ", "
		self.q = self.q[:-2]
		self.q += ")"
		self.tableControl()

while True:
	q = get_query()
	if q == '':
		break;
	try:
		#print("hoho")
		db.ping(reconnect=True)
		#print("hoho2")
		cur.execute(q)
		#print("hoho3")
		rows = cur.fetchall()
		
		#print("hoho4")
		print(rows)
		#print("hoho5")
		#print()
	except Exception as e:
		print('ERROR({no}): {value}'.format(no = e.args[0], value = e.args[1]))
		#print()

db.close()

entities = make_query('contentsData')
keywrdTable = Table("keywords")
keywrdTable.createTable("name char(30), activity char(20), location char(20), intimacy char(20), time char(20), keywords char(100), pic char(100), url char(100), weather char(20)")
for entity in entities:
	keywrdTable.insertValue(entity)
#testTable.insertValue(["'seyeon'", 1])

while True:
	q = get_query()
	if q == '':
		break;
	try:
		#print("hoho")
		db.ping(reconnect=True)
		#print("hoho2")
		cur.execute(q)
		#print("hoho3")
		rows = cur.fetchall()[0][0]
		
		#print("hoho4")
		print(rows)
		#print("hoho5")
		#print()
	except Exception as e:
		print('ERROR({no}): {value}'.format(no = e.args[0], value = e.args[1]))
		#print()

db.close()


