#soundcrawl.py
#crawl and output your friend's favorite songs. + your recent dashboard songs
#Idon't know what i'm doing.
#v084
import soundcloud


client = soundcloud.Client(
	client_id='',
	client_secret='',
	username='',
	password='')

text = open("test.txt", "w")
followers = client.get('/me/followings')
dashboard = client.get('/me/activities/tracks').collection

for users in followers:
	user = users
	o = 0
	favs = client.get ('/users/%s/favorites'%(user.permalink), limit = 200, offset = o)
	while favs:
		favs = client.get ('/users/%s/favorites'%(user.permalink), limit = 200, offset = o)
		o = o+200
		for x in favs:
			print x.permalink_url
			text.write(x.permalink_url + '\n')
			
for track in dashboard:
        text.write(track['origin']['permalink_url'] + '\n')
        print track['origin']['permalink_url']
