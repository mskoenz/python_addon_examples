#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    17.02.2015 09:52:54 CET
# File:    test_plot.py

from addon import *

import sys

def suit_1():
    #=================== convert txt file ===================
    cmd = namespace()
    cmd.arg = ["test_data/cos.txt", "test_data/sin.txt"]
    cmd.conv = "test_results"
    cmd.comment = ["#"]
    cmd.usetex = 1
    
    plot(cmd)
    
    #=================== update xml file ===================
    cmd = namespace()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.flag = ["update"]
    
    plot(cmd)
    
    #=================== parallel plot ===================
    cmd.clear()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.flag = ["parallel"]
    cmd.x = "#1"
    cmd.y = "#2"
    cmd.usetex = 1
    cmd.o = "test_results"
    
    plot(cmd)
    
    #=================== cp_opt plot ===================
    cmd.clear()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.cp_opt = [0,2]
    
    plot(cmd)
    
    #=================== joined plot ===================
    cmd.clear()
    cmd.arg = ["test_results/cos.xml", "test_results/sin.xml"]
    cmd.flag = []
    cmd.x = "#x"
    cmd.xlabel = "foo"
    cmd.ylabel = ["cos", "sin"]
    cmd.dsel = [100,-100,10]
    cmd.style = ["r^-","b^-"]
    cmd.y = ["_00_cos", "_01_sin"]
    cmd.usetex = 1
    cmd.o = "test_results/join.pdf"
    
    plot(cmd)
    
def suit_2():
    #=================== convert txt file ===================
    cmd = namespace()
    cmd.arg = ["test_data/test_{}.txt".format(n) for n in range(4)]
    cmd.conv = "test_results"
    cmd.comment = ["#"]
    
    plot(cmd)
    
    #=================== parallel plot ===================
    cmd.clear()
    cmd.arg = ["test_results/test_{}.xml".format(n) for n in range(4)]
    cmd.flag = ["parallel"]
    cmd.x = "x"
    cmd.y = "#4"
    cmd.o = "test_results"
    cmd.usetex = 1
    
    plot(cmd)
    
    #=================== joined plot ===================
    cmd.clear()
    cmd.arg = ["test_results/test_{}.xml".format(n) for n in range(4)]
    cmd.flag = []
    
    cmd.x = "#x"
    cmd.xlabel = "foo"
    cmd.y = "#4"
    cmd.xlabel = "{l} {N}"
    cmd.ylabel = "{#}-{L}"
    cmd.title = "number {N}"
    cmd.ylim = [0,100]
    cmd.yticks = [0,140,20]
    cmd.border = .02
    cmd.parameter = "all"
    cmd.fontsize = 20
    cmd.style = ["r^-","b^-","g^-","y^-"]
    cmd.usetex = 1
    cmd.o = "test_results/join_test.pdf"
    
    plot(cmd)
    
    
if __name__ == "__main__":
    print("test_plot.py")
    
    suit_1()
    suit_2()
