#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    23.03.2015 10:55:18 CET
# File:    example.py

import sys

import example_grammar as g
import example_grammar_ast as ast

from addon import *

if __name__ == "__main__":
    print("example.py")
    
    expr = "1/(4/4)*(5+1)/4"
    
    REDB(expr)
    
    p1 = parser()
    p1.set_grammar(g)
    res = p1.parse(expr)
    GREENB(res)
    
    p2 = parser(ast)
    res = p2.parse(expr)
    YELLOWB(res)
    
