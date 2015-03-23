#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    23.03.2015 10:56:12 CET
# File:    grammar.py

tokens = {"+": "ADD"
        , "-": "ADD"
        , "*": "MUL"
        , "/": "MUL"
        , "(": "LPAR"
        , ")": "RPAR"
        , "=": "ASS"
        }
match_rest = "NUM"
match = "[\w.]+"

rules = {
      "assign" :  ["id ASS sum"]
    , "sums" :    ["sums ADD products", "products"]
    , "products": ["products MUL atomic", "atomic"]
    , "atomic":   ["LPAR sums RPAR", "value"]
    , "value":    [match_rest]
    }

functions = {
      "assign":   lambda *args: args[2]
    , "sums":     lambda *args: args[0] if len(args) == 1 else args[0] + args[2] if args[1] == "+" else args[0] - args[2]
    , "products": lambda *args: args[0] if len(args) == 1 else args[0] * args[2] if args[1] == "*" else args[0] / args[2]
    , "atomic":   lambda *args: int(args[0]) if len(args) == 1 else args[1]
    , "value":    lambda *args: int(args[0])
    }
