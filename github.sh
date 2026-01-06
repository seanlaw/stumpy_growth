#!/bin/sh

SLACK_WEBHOOK="$1"
HOSTNAME="Github Actions"
STUMPY_STATS=`python3 get_stumpy_growth.py`
#echo $STUMPY_STATS

curl -k -X POST -H 'Content-type: application/json' --data "{\"text\":\"Server: $HOSTNAME\n$STUMPY_STATS\n\"}" $SLACK_WEBHOOK -o /dev/null
