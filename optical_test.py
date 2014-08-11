#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.08.2014 20:19:30 CEST
# File:    optical_test.py

from addon import *

if __name__ == "__main__":
    print("optical_test.py")
    N = 10000
    for i in range(N):
        print(progress_bar(i / float(N-1)) + RENTER)
    print()
