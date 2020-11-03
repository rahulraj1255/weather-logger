#!/bin/bash
#This script assumes that keep_part is greater than keep whole
keep_whole=7
keep_part=30
whole=(debug_log)
part=(debug_log)
for i in $(seq 0 $keep_part); do
	curdate=$(date --date "today - $i day" "+%Y_%m_%d")
	part+=($curdate)
	if [ $keep_whole -ge $i ]; then
		whole+=($curdate)
	fi
done

# Delete old files
find ~/logs_weather -type f $(printf "! -name %s " ${part[*]}) -exec rm -v {} \;

#Modify 
files=$(find log_folder/ -type f $(printf "! -name %s " ${whole[*]}))
for file in ${files[@]}; do
	echo Processing file $file
	tail -n 1 $file > tempfile
	mv tempfile $file
# > $file
done
