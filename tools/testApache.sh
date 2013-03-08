#!/bin/bash

LANG="../fedoraproject.org/po/LINGUAS"
WEBSITE="http://start.fedoraproject.org"

[[ -f $LANG ]] || exit 1

for l in `cat $LANG`
do
  status=`curl -is $WEBSITE/$l/ |grep Content-Type`
  echo $status | egrep -qE "html"
  [[ $? -eq 0 ]] || echo "$l: $status"
done
