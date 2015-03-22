#!/usr/bin/env bash

# load dependencies
apt-get install python-numpy

# set permissions
chmod a+x ./src/WordCount.py

# execute with RunningMedianHashTracker implementation
python ./src/WordCount.py

# uncomment if you want to run with RunningMedianSimple implementation
# python ./src/WordCount.py --running_median_method='simple'
