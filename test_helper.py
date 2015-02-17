#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    17.02.2015 10:29:43 CET
# File:    test_helper.py

import sys

from addon import *

if __name__ == "__main__":
    #=================== create_folder ===================
    GREENB("create_folder")
    bash("rm -rf test_results/foo")
    create_folder("test_results/foo/bar")
    create_folder("./test_results/foo/baz/")
    create_folder(abspath(__file__) + "/test_results/foo/zoo/")
    
    #=================== path ===================
    GREENB("path")
    DEBUG_VAR(path("./foo.txt"))
    DEBUG_VAR(filename("./foo.txt"))
    DEBUG_VAR(filetype("foo.txt"))
    DEBUG_VAR(abspath("./foo.txt"))
    
    #=================== list related stuff ===================
    GREENB("list related stuff")
    li = [[1, 2, 3, 4], [5, 6, 7, 8]]
    DEBUG_VAR(li)
    DEBUG_VAR(transpose(li))
    DEBUG_VAR(depth(li))
    DEBUG_VAR(flatten(li))
    DEBUG_VAR(nested_len(li))
