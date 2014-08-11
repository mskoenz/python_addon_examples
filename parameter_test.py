#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.08.2014 19:24:38 CEST
# File:    parameter_test.py

import sys
from addon.parameter import *

if __name__ == "__main__":
    print("parameter_test.py")
    
    p = parameter
    
    p["N"] = 1
    p["print_"] = True
    p["warn_"] = True
    
    custom = ["-p -ls", "-q"]
    p.read(sys.argv + custom) 
    
    if p.has_flag("p"):
        print(p)
    
    bash_if("ls", "echo foo")
    
    bash("echo bar")
    
    res = popen("ls")
    print(res)
