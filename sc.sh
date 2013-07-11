curl http://api.soundcloud.com/users/$user/tracks.json?client_id=YOUR_CLIENT_ID|sed  's/\,/\n/g'|grep permalink_url|sed "\/\"permalink_url\":\"http:\/\/soundcloud.com\/$user\"/d" >> ~/test.txt
