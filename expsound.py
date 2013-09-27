# expsound.py v0.15 proof of concept
# Using the experimental soundcloud API, finally gather only links that were favorited after x date
# to do: speed it up, write to file, idk


import soundcloud
import json
import urllib
from datetime import *

client = soundcloud.Client(
        client_id='',
        client_secret='',
        username='',
        password='')

def sound(uri):
        bytes = urllib.urlopen(uri)
        test = bytes.read()
        m = json.loads(test)
        return m

followers = client.get('/me/followings')

for users in followers:
        o = 0
        #uri = "https://api.soundcloud.com/e1/users/%s/likes.json?client_id=YOUR_CLIENT_ID&limit=200&offset=%s"%(users.id,o)
        m = True
        while m:
                uri = "https://api.soundcloud.com/e1/users/%s/likes.json?client_id=YOUR_CLIENT_ID&limit=200&offset=%s"%(users.id,o)
                m = sound(uri)
                o = o + 200
                for songs in m:
                        created = songs['created_at']
                        cre = datetime.strptime(created[:19], "%Y/%m/%d %H:%M:%S")
                        bef = datetime.today() - timedelta(days=26)
                        if bef < cre:
                                try:
                                        print songs['track']['permalink_url'], cre
                                except TypeError:
                                        print "Playlist maybe"
                                        #print cre, bef < cre
