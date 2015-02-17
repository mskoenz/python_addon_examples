#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    15.01.2015 09:15:04 CET
# File:    state_test.py

import sys
import time

from addon import *

if __name__ == "__main__":
    print("state_test.py")
    d = "test_data"
    p = 0
    while p < 1:
        p = read_status(d)["p"]
        print(progress_bar(p))
        time.sleep(.1)
