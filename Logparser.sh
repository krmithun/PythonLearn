#!/bin/bash
#This script should return a set of lines between 2 values, the main purpose is for searching a log file between 2 times
#Script usage: logship.sh "start" "stop" file

#If the file contains any "/" in the date range the following 2 lines add the escape character so that the search can be performed for those characters
start=$(echo "$1" | sed 's/\//\\\//g')
stop=$(echo "$2" | sed 's/\//\\\//g')

zipped=$(echo "$3" | grep -c "gz$")     #figures out if the file is zipped or not

if [ "$zipped" ==  "1" ]; then          #If the file is zipped then pass it through zcat before sed
        zcat $3 | sed -n "/$start/,/$stop/p";
else
        sed -n "/$start/,/$stop/p" $3;  #if it's not zipped just run sed
fi