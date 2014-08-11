#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.08.2014 19:55:29 CEST
# File:    qt_test.py

import sys
from addon.qt4 import *
#~ from addon.qt5 import *

if __name__ == "__main__":
    print("qt_test.py")
    
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    app.exec_()
    
