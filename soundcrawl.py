#I don't know what i'm doing.
import soundcloud


client = soundcloud.Client(
	client_id='',
	client_secret='',
	username='',
	password='')

text = open("test.txt", "w")
followers = client.get('/me/followings')

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
			#client.get ('/users/user/favorites', created_at = { 'from':'2012-08-29 12:13:23'}) (used to file songs by date)
