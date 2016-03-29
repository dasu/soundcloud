# expsound.py v0.30 proof of concept
# Using the experimental soundcloud API, finally gather only links that were favorited after x date
# soundcloud 0.5.0 module
# to do: documentations
import soundcloud
import requests
import sys
from datetime import *

client = soundcloud.Client(
	client_id='',
	client_secret='',
	username='',
	password='')

def sound(uri):
	return requests.get(uri).json()

text = open("test5.txt", "w")
followers = client.get('/me/followings').collection
dashboard = client.get('/me/activities/tracks').collection

for users in followers:
        o = 0
        m = True
        while m:
                print users.id
                uri = "https://api.soundcloud.com/e1/users/%s/likes.json?client_id=API_KEY_GOES_HERE&limit=200&offset=%s"%(users.id,o)
                m = sound(uri)
                o = o + 200
                i = 1
                for songs in m:
                        created = songs['created_at']
                        cre2 = datetime.strptime(created[:19], "%Y/%m/%d %H:%M:%S")
                        cre = cre2.date()
                        bef2 = (datetime.strptime(sys.argv[1],"%Y-%m-%d")) - timedelta(days=1)
                        bef = bef2.date()
                        if bef <= cre:
                                try:
                                        print songs['track']['permalink_url'], cre
                                        text.write(songs['track']['permalink_url'] + '\n')
                                except TypeError:
                                        print "Playlist maybe"
                                        #print cre, bef < cre

for track in dashboard:
        text.write(track.origin.permalink_url + '\n')
        print track.origin.permalink_url
