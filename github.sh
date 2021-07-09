#!/bin/sh

HOSTNAME=`Github Actions`
STUMPY_STATS=`python3 get_stumpy_growth.py 2> /dev/null`
echo $STUMPY_STATS

curl -k -X POST -H 'Content-type: application/json' --data "{\"text\":\"Server: $HOSTNAME\n$STUMPY_STATS\n\"}" https://hooks.slack.com/services/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 -o /dev/null
