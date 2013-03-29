#!/bin/sh

set -e

TARBALL=countdown-banners.tar.gz

wget http://ryanlerch.fedorapeople.org/countdown-banner/$TARBALL
tar xzf $TARBALL
rm $TARBALL

for i in `ls *.gz`
do
  lang=`echo $i |sed -n 's/fedora18-countdown-banner-\(.*\)\.tar.gz/\1/p'`
  mkdir $lang
  tar xzf $i -C $lang
  rm $i
done


exit 0

while read -r line
do
   file="fedora17-countdown-banner-$line.tar.gz"
   mkdir $line
   cd $line
   wget "http://inkscaper.fedorapeople.org/Fedora17/countdown-banner/$file"
   tar xzf $file && rm $file
   cd ..
done < lang
