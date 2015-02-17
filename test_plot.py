#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    17.02.2015 09:52:54 CET
# File:    test_plot.py

from addon import *

import sys

if __name__ == "__main__":
    print("test_plot.py")
    
    #=================== convert txt file ===================
    cmd = namespace()
    cmd.arg = ["test_data/cos.txt", "test_data/sin.txt"]
    cmd.conv = "test_results"
    cmd.comment = ["#"]
    
    plot(cmd)
    
    #=================== update xml file ===================
    cmd = namespace()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.flag = ["update"]
    
    plot(cmd)
    
    #=================== cp_opt plot ===================
    cmd.clear()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.cp_opt = [0,2]
    
    plot(cmd)
    
    #=================== parallel plot ===================
    cmd.clear()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.flag = ["plot", "parallel"]
    cmd.x = "x"
    cmd.y = 2
    cmd.o = "test_results"
    
    plot(cmd)
    
    #=================== joined plot ===================
    cmd.clear()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.flag = ["plot"]
    cmd.x = "00-x"
    cmd.xlabel = "foo"
    #~ cmd.ylabel = ["cos", "sin"]
    cmd.style = ["r-","b-"]
    cmd.y = ["00-cos", "01-sin"]
    cmd.o = "test_results/join.pdf"
    
    plot(cmd)
