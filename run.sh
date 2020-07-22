#!/bin/sh

PYTHON="/home/law978/miniconda3/bin/python"
HOSTNAME=`uname -n`
APPDIR="$( cd "$( dirname "$0" )" && pwd )"
STUMPY_STATS=`$PYTHON $APPDIR/get_stumpy_growth.py 2> /dev/null`

curl -k -X POST -H 'Content-type: application/json' --data "{\"text\":\"Server: $HOSTNAME\n$STUMPY_STATS\n"}" https://hooks.slack.com/services/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 -o /dev/null
