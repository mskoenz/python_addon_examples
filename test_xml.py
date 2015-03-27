#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    26.03.2015 09:08:59 CET
# File:    test_xml.py

import sys

from addon import *

if __name__ == "__main__":
    print("test_xml.py")
    p = xml_parser("./test_data/plot_data.xml")
    
    ns = namespace()
    ns.x = 1000000000000000000000000000000000000000000000000000000000000000000000000000000
    print(ns)
    
    print(p)
    print(p.plot_option)
    print(p.plot_option.param())
    print(p.label)
    print(p.data.info())
    print(p.data.d[0].value())
    print(p.parameter["H"])

