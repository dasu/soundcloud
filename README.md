soundcloud
==========

Simple shell scripts to scrape soundloud links to be used for whatever program you want (such as j-downloader)

sc.sh usage: bash sc.sh name_of_user
example: bash sc.sh mossya
Will create test.txt on user folder with every sound link the user has publically available, by most recent sound.

sc2.sh usage: bash sc2.sh name_of_user offset_number
example: bash sc2.sh mossya 0
Will create test.txt on user folder with every sound link in the user's favorite by most recent favorite.  Offset is used to go further than the 200 (or is it more?) limit.  


TO DO:
remove "permalink_url": OR use a json parser
automate it a bit more
wakaranai
