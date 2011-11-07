#!/bin/sh
# this script pull all translations to transifex,
#      and then fill the LINGUAS file
#      It could also make POT and push them… If you comment out what needed.
# usage: `basename $0` [website]
#      if no website specified, the whole array "site" would be parsed.
## TODO: to add the --commit feature

site=( boot.fedoraproject.org 
       fedoracommunity.org
       fedorahosted.org
       fedoraproject.org
       fudcon.fedoraproject.org
       spins.fedoraproject.org
       start.fedoraproject.org
       talk.fedoraproject.org )


# "linguas_update website" update the LINGUAS file by adding all language code where translations have started
function linguas_update {
  PO_PATH="$1/po"
  LINGUAS="$PO_PATH/LINGUAS"
   
  
  if [ ! -f $LINGUAS ]
  then
     echo "No $LINGUAS file there"
  fi
  
  tmp="l_tmp"
  sed -i 's#\s##g' $LINGUAS                   # remove trailing whitespaces
  
  for file in `ls $PO_PATH/*.po`
  do
    stat=`msgfmt -c --statistics $file 2>&1 | awk '{print $1}'`
    if [ "$stat" != "0" ]                     # if translation is started
    then                                 
      lang=`echo $file| sed -n "s#.*/\(.*\).po#\1#p" `   # filter the language code
      echo $lang >> $tmp                      # add it in a temp file
      new=`grep $lang"\$" $LINGUAS`
      if [ "@$new" == "@" ]                   # if this language code is new
      then
        echo "$lang added, translated strings=$stat"
      fi
    fi
  done
  
  rm $LINGUAS
  cat $tmp|sort > $LINGUAS
  rm $tmp
}


# if no argument specified, parse all websites
if [ -z $1 ]
then
  echo "Going to update the following websites:"
  echo "${site[*]}"
else
  echo "Going to update $1"
  if [ ! -d $1 ]
  then
     echo "$1 not found!"
     exit 111
  fi
  site=( $1 )
fi


for i in "${site[@]}"
do
   echo "- Updating $i POs and POT"
   cd $i
   make pullpos
#   git add po/*.po
#   make pot && make pushpot 
#   git add po/*.pot
   cd ..
   echo "- Updating $i LINGUAS file"
   linguas_update $i   # LINGUAS changes won't be automatically added in git, you probably want a different commit
done

# git commit -m "Full POs update"

