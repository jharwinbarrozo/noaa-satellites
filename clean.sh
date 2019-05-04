#!/bin/sh

## debug
# set -x

. ~/.noaa.conf

find ${NOAA_HOME}/map/ -type f -name '*.png' -mtime +2 -exec rm -f {} \; 
#retain 2 days ago data

find ${NOAA_OUTPUT}/wav/audio/ -type f -name '*.wav' -mtime +2 -exec rm -f {} \;
#retain 2 days ago data
