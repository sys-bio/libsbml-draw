# -*- coding: utf-8 -*-

#You avoid most rounding errors by using

#Control1 = (Start + 2 * Control) / 3
#Control2 = (End   + 2 * Control) / 3
#Note that line segments are also convertible to cubic Bezier curves using:

#Control1 = Start
#Control2 = End

# https://stackoverflow.com/questions/50871343/connectionstyle-arc3-fancyarrowpatch-and-path-curve3-two-quadratic-bezier-cu