#!/bin/sh
#>>logs/luna.log 2>&1
git pull origin master &>>logs/luna.log
python3 luna.py