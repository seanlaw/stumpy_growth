#!/bin/sh

APPDIR="$( cd "$( dirname "$0" )" && pwd )"
STUMPY_STATS=`$APPDIR/get_stumpy_growth.py 2> /dev/null`
HOSTNAME=`uname -n`

curl -k -X POST -H 'Content-type: application/json' --data "{\"text\":\"Server: $HOSTNAME\n$STUMPY_STATS\"}" https://hooks.slack.com/services/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 -o /dev/null
