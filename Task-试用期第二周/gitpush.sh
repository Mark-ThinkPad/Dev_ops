#!/bin/sh

if [ $# == 1 ];
then
    git add .
    message=$1
    git commit -m "${message}"
    git push
else
    echo '[usage]'
    echo 'gitpush [COMMIT MESSAGE]'
fi
