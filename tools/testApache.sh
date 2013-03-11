#!/bin/bash
# Depends on curl
# Assumption:
# - The return code should not be 404
# - The Content-Type should be "text/html"
# - The Content-Language should reflect the Accept-Language provided
# TODO: check fedorahosted.org ?

LANG="po/LINGUAS"
OK="HTTP/1.1 200 OK"
CONTENTTYPE="Content-Type: text/html"
ROOT_PATH="$PWD/.."

site=( boot.fedoraproject.org
       fedoracommunity.org
       fedoraproject.org
       fudcon.fedoraproject.org
       spins.fedoraproject.org
       start.fedoraproject.org )

function check
{
	website=$1
	echo "=== Checking \`$website' ==="
	cd $ROOT_PATH/$1

	if [ ! -f $LANG ]
	then
		echo "\`$LANG' file not found, please provide the LINGUAS file path"
		exit 1
	fi

	for l in `cat $LANG`
	do
    l=${l/_/-}
    l=${l,,}
		status=`curl -Iis $website --header "Accept-Language: $l"`

		# Checking the HTTP answer
    echo "$status" | egrep -qE "$OK"
		if [ $? -ne 0 ]; then
      res=`echo "$status" | head -n 1`
			echo "$l: ERROR: $res"
			continue
		fi

		# Checking the Content-Type
		echo "$status" | egrep -qE "$CONTENTTYPE"
		[[ $? -eq 0 ]] || echo "$l: `echo "$status"|grep "$CONTENTTYPE"`"

		# Checking the Content-Language
		locale=`echo "$status"|grep "Content-Language"|tr -d '\r'`
		if [ "$locale" != "Content-Language: $l" ]; then
      echo "$l: $locale"
    fi
	done
}

for i in "${site[@]}"
do
  check $i
done


