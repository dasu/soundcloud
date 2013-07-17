import json
import urllib
from openpyxl import load_workbook

#users = []
#favn = []
#list = []
y = 2
tel = {}
uri = 'http://api.soundcloud.com/users/dasu/followings.json?client_id=YOUR_CLIENT_ID'
bytes = urllib.urlopen(uri)
test = bytes.read()
m = json.loads(test)
for name in m:
  user = name['permalink']
	fav = name['public_favorites_count']
#	users.append(user)
#	favn.append(fav)
	tel[user] = fav
	
#if users == []:
#	print 'Nothing found'
#else:
#	print (",".join(users))
#	print (",".join(str(w) for w in favn))

wb2 = load_workbook('test.xlsx')
sheet1 = wb2.get_sheet_by_name(name= 'Sheet1')
x = sheet1.get_highest_column()
print 'x = ' + str(x)
print 'y = ' + str(y)
for row in sheet1.range('A3:A25'):
	for p in row:
		cv = sheet1.cell(row = y, column = x)
		cv.value = tel[p.value]
		print cv.value
		y += 1		
#		print y
#		list.append(p.value)
#		print tel[p.value]
		#print p.value + ' has ' + str(tel[p.value])
		


#while y < len(list):
#	if list[y] == users[0]:
#		print list[y] + ' true'
#		y += 1
#	else:
#		print list[y] + ' false'
#		y += 1
#		
#if not sheet1.cell('A3').value:
#	print 'Cell has no value'
#else:
#	print 'Cell has value:'
#	print sheet1.cell('A3').value

#print tel['posse-1']
print sheet1.get_highest_column()
wb2.save('test.xlsx')
