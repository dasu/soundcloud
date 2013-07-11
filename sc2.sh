#!/bin/bash
user="$1"
i="0"
while [ $i -lt $2 ]
do
   curl "https://api.soundcloud.com/users/$user/favorites.json?consumer_key=apigee&limit=200&offset=$i"|sed 's/\,/\n/g'|grep \"permalink_url\":\"http:\/\/soundcloud.com\/.*/.*\"|sed 's/\"permalink_url\"://g' >> ~/test.txt
i=$[$i+200]
done
