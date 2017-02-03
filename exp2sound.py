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

def get_songs(likes,setdate):
    for songs in likes['collection']:
        song_liked = datetime.strptime(songs['created_at'],"%Y-%m-%dT%H:%M:%SZ").date()
        cutoff = ((datetime.strptime(setdate,"%Y-%m-%d")) - timedelta(days=1)).date()
        if cutoff <= song_liked:
            try:
                if songs['track']:
                    print str(song_liked), songs['track']['permalink_url']
                    text.write(songs['track']['permalink_url'] + '\n')
            except KeyError:
                print str(song_liked), songs['playlist']['permalink_url']
                text.write(songs['playlist']['permalink_url'] + '\n')
        else:
            print("returning false...")
            return False
    return True

text = open("api2.txt", "w")
followers = client.get('/me/followings').collection
dashboard = client.get('/me/activities/tracks',limit=200)
cutoff = ((datetime.strptime(sys.argv[1],"%Y-%m-%d")) - timedelta(days=1)).date()
while dashboard:
    for tracks in dashboard.collection:
        if tracks.origin.obj:
            created_at = datetime.strptime(tracks.origin.obj['created_at'][:19],"%Y/%m/%d %H:%M:%S").date()
            if cutoff <= created_at:
                text.write(tracks.origin.permalink_url + '\n')
    try:
        dashboard = client.get(dashboard.next_href,limit=200)
    except:
        break

for users in followers:
    print users.permalink_url
    uri = "https://api-v2.soundcloud.com/users/{0}/likes?limit=200&client_id=CLIENT_ID_GOES_HERE".format(users.id)
    likes = sound(uri)
    if not get_songs(likes,sys.argv[1]):
        continue
    while likes['next_href']:
        likes = sound(likes['next_href']+"&client_id=CLIENT_ID_GOES_HERE")
        if not get_songs(likes,sys.argv[1]):
            break
        if likes['next_href'] is None:
            break

print("Reached end of script")
