#!/bin/bash
#compares both output of old and new reports from soundcrawl and outputs the differences between the two.
# useful for just grabbing whatever has changed.
#v.23

date=$(date +%F)

python ./soundcrawl.py

echo "Sorting now"

sort -u ./new.txt -o ./new.txt

comm -3 ./new.txt ./old.txt| sed 's/^\t//' > ./diff.txt

mv ./old.txt ./old/old-$date.txt

mv ./new.txt ./old.txt
