#!/bin/bash
# this script pull all translations to transifex,
#      make an new POT and push it if asked,
#      and then fill the LINGUAS file

site=( boot.fedoraproject.org 
       fedoracommunity.org
       fedorahosted.org
       fedoraproject.org
       fudcon.fedoraproject.org
       spins.fedoraproject.org
       start.fedoraproject.org )


usage()
{
cat << EOF
usage: $0 [OPTIONS] [-w WEBSITE]

This script update all L10n things. Will never git push.
 * pull translations from transifex against WEBSITE in current branch
 * make new POT in WEBSITE
 * update the LINGUAS file in WEBSITE

OPTIONS:
   -h      Show this message
   -a      Git add all 
   -c      With -a, git commit with default message (POs, POT and LINGUAS in different commits)
   -p      With -c make pushpot (update POT on transifex.net)

WEBSITE:
    The website targeted (like "fedoraproject.org")
    Without WEBSITE specifyed, will parse the whole website array.

EXAMPLES:
         $ $0                                  (1)
         $ $0 -a spins.fedoraproject.org       (2)
         $ $0 -a -c -p                         (3)

   1. Update all but let you git add and push to transifex.net. (Takes time but let you do the job). 
   2. Update POs POT and LINGUAS of spins.fedoraproject.org website. Let you commit and push (git/transifex).
   3. Update all and commit changes in 3 different commits. That's what you were looking for.

EOF
}

while getopts ":hacpw:" OPTION
do
  case $OPTION in
    h)
      usage
      exit 1
      ;;
    a)
      ADD=1
      ;;
    c)
      COMMIT=1
      ;;
    p)
      TXN_PUSH=1
      ;;
    w)
      WEBSITE=$OPTARG
      ;;
    ?)
      usage
      exit
      ;;
  esac
done


if [ -z $WEBSITE ]
then
  echo "Going to update the following websites:"
  echo "${site[*]}"
else
  echo "Going to update $WEBSITE"
  if [ ! -d $WEBSITE ]
  then
     echo "$WEBSITE not found!"
     exit 111
  fi
  site=( $WEBSITE )
fi


### POs

echo "- Updating POs"
for i in "${site[@]}"
do
   cd $i
   make pullpos
   if [ ! -z $ADD ]
   then
     git add po/*.po
   fi
   cd ..
done

if [ ! -z $COMMIT ] && [ ! -z $ADD ]
then
  git commit -m "[`basename $0`] Full POs update"
fi


### POT

echo "- Updating POT"
for i in "${site[@]}"
do
   cd $i
   make pot
   insertion_number=`git diff --numstat po/*.pot 2>&1 | awk '{print $1}'` # record the number of insertion,
									 #if no new string found at least the build time could change (i.e. check if > 1)
   let "$((++insertion_number))"     # cause in case the file is exactly the same, prevent no git diff output
   if [ $insertion_number -gt 2 ]
   then								 # POT should be uploaded
     NEED_COMMIT=1					 # don't commit if any POT modified!
     if [ ! -z $ADD ]
     then
       git add po/*.pot
       if [ ! -z $TXN_PUSH ] && [ ! -z $COMMIT ]
       then
         make pushpot
       fi
     fi
     echo "POT updated"
   else
       git checkout -- po/*.pot     # no real change, undo (only the build time was changed)
   fi
   cd ..
done

if [ ! -z $NEED_COMMIT ] && [ ! -z $COMMIT ] && [ ! -z $ADD ]
then
  git commit -m "[`basename $0`] Full POT update"
fi

### LINGUAS
# update the LINGUAS file by adding all language code where translations have started

echo "- Updating LINGUAS file"
for i in "${site[@]}"
do
  PO_PATH="$i/po"
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

  git diff --exit-code $LINGUAS > /dev/null   # check if modified
  if [ $? -eq  1 ] && [ ! -z $ADD ]
  then
    git add $LINGUAS
    L_COMMIT=1
  fi
done

if [ ! -z $L_COMMIT ] && [ ! -z $COMMIT ] && [ ! -z $ADD ]
then
  git commit -m "[`basename $0`] Full LINGUAS update"
fi


exit 0
