#!/bin/sh

while read -r line
do
   file="fedora17-countdown-banner-$line.tar.gz"
   mkdir $line
   cd $line
   wget "http://inkscaper.fedorapeople.org/Fedora17/countdown-banner/$file"
   tar xzf $file && rm $file
   cd ..
done < lang
