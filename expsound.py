# expsound.py v0.30 proof of concept
# Using the experimental soundcloud API, finally gather only links that were favorited after x date
# to do: speed it up, write to file, idk


import soundcloud
import requests
from datetime import *

client = soundcloud.Client(
        client_id='',
        client_secret='',
        username='',
        password='')

def sound(uri):
        return requests.get(uri).json()

text = open("test5.txt", "w")
followers = client.get('/me/followings')
dashboard = client.get('/me/activities/tracks').collection

for users in followers:
        o = 0
        m = True
        while m:
                uri = "https://api.soundcloud.com/e1/users/%s/likes.json?client_id=YOUR_CLIENT_ID&limit=200&offset=%s"%(users.id,o)
                m = sound(uri)
                o = o + 200
                i = 1
                for songs in m:
                        created = songs['created_at']
                        cre2 = datetime.strptime(created[:19], "%Y/%m/%d %H:%M:%S")
                        cre = cre2.date()
                        #bef = datetime.today() - timedelta(days=26)
                        bef = date(2013,11,26)
                        if bef < cre:
                                try:
                                        print songs['track']['permalink_url'], cre
                                        text.write(songs['track']['permalink_url'] + '\n')
                                except TypeError:
                                        print "Playlist maybe"
                                        #print cre, bef < cre

for track in dashboard:
        text.write(track['origin']['permalink_url'] + '\n')
        print track['origin']['permalink_url']
