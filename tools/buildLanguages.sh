#!/bin/bash
LINGUAS_TMP="LINGUAS_TMP"
LINGUAS="LINGUAS"
ROOT_PATH="$PWD/.."
PRE="/srv/web"
TMP="$ROOT_PATH/httpd/conf"

declare -A site

site=( ["boot.fedoraproject.org"]="boot-languages.conf"
       ["fedoracommunity.org"]="fedoracommunity.org-languages.conf"
       ["fedoraproject.org"]="languages.conf"
       ["fudcon.fedoraproject.org"]="fudcon-languages.conf"
       ["spins.fedoraproject.org"]="spins-languages.conf"
       ["start.fedoraproject.org"]="start-languages.conf" )

function build
{
	cd $ROOT_PATH/$1
  python $ROOT_PATH/build.d/buildconf.py $ROOT_PATH/$LINGUAS > ${site[$1]}
  sed -i "s#@DOCUMENTROOT@#$PRE/$1#g" ${site[$1]}
  mv ${site[$1]} $TMP
}

cd $ROOT_PATH
# Fill a complete LINGUAS file
cat `find . -name LINGUAS` >> $LINGUAS_TMP
sort -u $LINGUAS_TMP -o $LINGUAS

# Build the language.conf file for every websites -- Used in puppet
for i in "${!site[@]}"
do
  build $i
done

cd $ROOT_PATH
rm $LINGUAS $LINGUAS_TMP

