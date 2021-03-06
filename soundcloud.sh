#!/bin/bash
#compares both output of old and new reports from soundcrawl and outputs the differences between the two.
# useful for just grabbing whatever has changed.
#v.40

set -e
date1=$(date +%F)
date2=$(date -r diff.txt +%F)

python ./soundcrawl.py
if [ $? -ne 0 ]; then
    exit 1
fi

echo "Sorting now"

sort -u ./new.txt -o ./new.txt

comm -3 ./new.txt ./old.txt| sed 's/^\t//' > ./diff.txt

mv ./old.txt ./old/old-$date1.txt

mv ./new.txt ./old.txt

python ./exp2sound.py $date2

cat ./api2.txt ./diff.txt > ./combined.txt

sed -i 's/https:\/\//http:\/\//g' combined.txt

sort -u ./combined.txt -o ./combined.txt
