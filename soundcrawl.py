#soundcrawl.py
#crawl and output your friend's favorite songs. + your recent dashboard songs
#soundcloud v0.5.0 module
#v088
import time
from urllib2 import HTTPError
import soundcloud


client = soundcloud.Client(
        client_id='',
        client_secret='',
	username='',
	password='')

text = open("new.txt", "w")
followers = client.get('/me/followings').collection
dashboard = client.get('/me/activities/tracks').collection

for users in followers:
	user = users
	o = 0
	print users.permalink
	try:
		favs = client.get ('/users/%s/favorites'%(user.permalink), limit = 200, offset = o)
	except HTTPError, e:
		print e
		continue
	while favs:
		time.sleep(1)
		try:
			favs = client.get ('/users/%s/favorites'%(user.permalink), limit = 200, offset = o)
		except HTTPError, e:
			o=o+200
			print e
			continue
		o = o+200
		for x in favs:
			text.write(x.permalink_url + '\n')
			print x.permalink_url

for track in dashboard:
	if track.origin.obj:
		text.write(track.origin.permalink_url + '\n')
		print track.origin.permalink_url
