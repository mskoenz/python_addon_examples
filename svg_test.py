#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    27.08.2014 09:46:09 CEST
# File:    svg_text.py

from addon.svg import *

def main():
    pic = canvas(height = 400, width = 400)
    pic.add(lingrad(id = "A", color1 = "red", color2 = "yellow", dir = "dr"))
    pic.add(lingrad(id = "B", color1 = "blue", color2 = "yellow", dir = "lu"))
    gp = group(stroke = "black", stroke_width = 1)
    pic.add(gp)
    pic.add(rect(xy = (100, 100), size = (200, 200), fill = 'cyan'))
    gp.add(line(xy1 = (200, 200), xy2 = (200, 300)))
    gp.add(line(xy1 = (200, 200), xy2 = (300, 200)))
    gp.add(line(xy1 = (200, 200), xy2 = (200, 100)))
    pic.add(line(xy1 = (200, 200), xy2 = (100, 200)))
    pic.add(circle(cxy = (200, 200), r = 30, fill = "blue"))
    pic.add(circle(cxy = (200, 300), r = 30, fill = "green"))
    pic.add(circle(cxy = (300, 200), r = 30, fill = "red"))
    pic.add(circle(cxy = (100, 200), r = 30, fill = "B"))
    pic.add(circle(cxy = (200, 100), r = 30, fill = "A"))
    pic.add(text(xy = (50, 50), text = "Testing SVG", font_size = 24, color = "black"))
    pic.write_svg("test_results/test.svg")
    pic.display()

if __name__ == "__main__":
    main()
