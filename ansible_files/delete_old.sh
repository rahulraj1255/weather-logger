#!/bin/bash
#This script assumes that del_old_than is greater than mod_old_than
del_old_than=30
mod_old_than=7
not_del=(debug_log)
not_mod=(debug_log)
for i in $(seq 0 $del_old_than); do
	curdate=$(date --date "today - $i day" "+%Y_%m_%d")
	not_del+=($curdate)
	if [ $mod_old_than -ge $i ]; then
		not_mod+=($curdate)
	fi
done

# Delete old files
find ~/logs_weather -type f $(printf "! -name %s " ${not_del[*]}) -exec rm -v {} \;

#Modify 
files=$(find log_folder/ -type f $(printf "! -name %s " ${not_mod[*]}))
for file in ${files[@]}; do
	echo Processing file $file
	tail -n 1 $file > tempfile
	mv tempfile $file
# > $file
done
