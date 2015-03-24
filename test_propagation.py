#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    23.03.2015 21:42:31 CET
# File:    test_propagation.py

import sys
from addon import *

if __name__ == "__main__":
    print("test_propagation.py")
    np.random.seed(0)
    label = ["foo", "foo_err", "bar", "bar_err"]
    data  = [ [100 + np.random.normal() for i in range(3)]
            , [abs(np.random.normal()) for i in range(3)]
            , [200 + np.random.normal() for i in range(3)]
            , [abs(np.random.normal()) for i in range(3)]
            ]
    
    #------------------- expression -------------------
    instring = "trig_conv(2)@acc2@(foo)+bar/23"
    
    #------------------- custom matrix -------------------
    gen.matrix.acc2 = lambda *args: np.add.accumulate
    
    
    YELLOWB(instring)
    
    val, err = calc_expr(label, data, instring)
    
    GREEN(data[label.index("foo")])
    GREEN(data[label.index("foo_err")])
    
    YELLOW(data[label.index("bar")])
    YELLOW(data[label.index("bar_err")])
    
    RED(val)
    RED(err)
