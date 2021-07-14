#!/bin/bash
# Usage
# ls-httpd type count
# Eg:
# ls-httpd url 1000
# will find top URLs in the last 1000 access log entries
# ls-httpd ip 1000
# will find top IPs in the last 1000 access log entries
# ls-httpd agent 1000
# will find top user agents in the last 1000 access log entries

type=$1
length=$2

if [ "$3" == "" ]; then
  log_file="/var/log/httpd/example.com-access_log"
else
  log_file="$3"
fi

if [ "$type" = "ip" ]; then
  tail -n $length $log_file | grep -o "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" | sort -n | uniq -c | sort -n
elif [ "$type" = "agent" ]; then
  tail -n $length $log_file | awk -F\" '{print $6}'| sort -n | uniq -c | sort -n
elif [ "$type" = "url" ]; then
  tail -n $length $log_file | awk -F\" '{print $2}'| sort -n | uniq -c | sort -n
fi