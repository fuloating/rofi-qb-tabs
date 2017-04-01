#!/bin/bash

TABFILE="$HOME/scripts/rofi/tabs"
ARG=$@

if [ -n "${ARG}" ]
then
    SEL_URL=$( echo ${ARG} | perl -ne 'if (/^(.+?)\s+(https?:\/\/\S+)\s*(.*)$/) {print "$2\n"}')
    coproc ( xdg-open "$SEL_URL" > /dev/null  2>&1 )
    exec 1>&-
    grep -v "$ARG" "$TABFILE" > "temp.txt"
    cp "temp.txt" "$TABFILE"
else
    cat "$TABFILE" | sed "/^$/d;/^#/d;/^\//d" | sort -n 
fi
