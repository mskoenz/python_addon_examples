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
      "assign":   lambda *args: args[0] if len(args) == 1 else list(args)
    , "sums":     lambda *args: args[0] if len(args) == 1 else list(args)
    , "products": lambda *args: args[0] if len(args) == 1 else list(args)
    , "atomic":   lambda *args: args[0] if len(args) == 1 else list(args)
    , "value":    lambda *args: args[0] if len(args) == 1 else list(args)
    }
