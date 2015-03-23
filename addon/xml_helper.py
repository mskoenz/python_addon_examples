#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    03.03.2015 09:24:12 CET
# File:    xml_helper.py

import xml.etree.ElementTree as xml

from .helper import *

def prettify(node, indent = "    ", level = 0):
    node.tail = "\n" + indent * level
    if len(node) != 0:
        node.text = "\n" + indent * (level + 1)
        for c in node:
            prettify(c, indent, level + 1)
            if c == node[-1]:
                c.tail = "\n" + indent * level
    else:
        if node.text:
            node.text = node.text.strip()
        node.tail = "\n" + indent * level

class xml_element():
    def __init__(self, root):
        self.root = root
    
    def __getattr__(self, key):
        res = self.root.findall(key)
        if len(res) == 0:
            ERROR("child {} not found".format(key))
        elif len(res) == 1:
            return xml_element(res[0])
        else:
            return [xml_element(r) for r in res]
    
    def __getitem__(self, key):
        return to_number(self.root.attrib[key])
    
    def __str__(self):
        os = ""
        os += self.root.tag
        return os
    
    def __repr__(self):
        return self.__str__()
    
class xml_parser(xml_element):
    def __init__(self, file_):
        self.file_ = file_;
        self.parse()
        super(xml_parser, self).__init__(self.root)
    
    def parse(self):
        self.tree = xml.parse(self.file_)
        self.root = self.tree.getroot()
