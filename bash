#! /bin/bash  

#echo `pwd`$(dirname $0)

execPath=$(readlink -f $(dirname $0))
echo $execPath



#alias touktouk="python /media/hdfs/user/iah/bin/count.py"
touktouk=$"${execPath}houhou"

echo $touktouk
alias touktouk="python ${execPath}/count.py"
