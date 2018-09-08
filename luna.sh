#!/bin/sh
git pull origin master &>> logs/luna.log
python3 luna.py