#
# Demo program for drawing Bezier curve using Python
#
# $Id: bezier.py,v 1.2 2005/05/09 21:16:28 exact Exp $
# 
# see http://www.doc.ic.ac.uk/~dfg/AndysSplineTutorial/Beziers.html 
# for an interactive bezier drawing applet
#
# if use corelib, then do the following
#
#   	from corelib import *
#	NT = BigFloat
#
# else use python's math library
#
#	from math import *
#	NT = float

import math
#from corelib import *
import bigfloat
NT = bigfloat.BigFloat
#from math import *
#NT = float

#from pylab import *
#from matplotlib.matlab import *
import matplotlib.pyplot as plt

# class Point
class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
	
    def distance(self, p):
        return math.sqrt((p.x-self.x)*(p.x-self.x)+(p.y-self.y)*(p.y-self.y))

    def length(self):
        return self.distance(Point(NT(0), NT(0)))

    def __sub__(self, p):
        return Point(self.x-p.x, self.y-p.y)

    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)

    def __mul__(self, c):
        return Point(c*self.x, c*self.y)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __ne__(self, p):
        return not (self == p)
	
    def towards(self, target, t):
        if t == 0.5:
            return self.halfway(target)
        else:
            return Point((1.0-t)*self.x+t*target.x, (1.0-t)*self.y+t*target.y)
	
    def halfway(self, target):
        return Point((self.x+target.x).div2(), (self.y+target.y).div2())

    def compare_lex(self, p):
        if self.x < p.x:
            return -1
        if self.x > p.x:
            return 1
        if self.y < p.y:
            return -1
        if self.y > p.y:
            return 1
        return 0

    def less_lex(self, p):
        return self.compare_lex(p) < 0

    def less_eq_lex(self, p):
        return self.compare_lex(p) <= 0
	
    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)  	

def orientation2d(a, b, c):
    d1 = (a.x - b.x) * (a.y - c.y)
    d2 = (a.y - b.y) * (a.x - c.x)
    if d1 == d2:
        return 0
    elif d1 > d2:
        return 1
    else:
        return -1

def leftTurn(a, b, c):
    return orientation2d(a, b, c) > 0

def rightTurn(a, b, c):
    return orientation2d(a, b, c) < 0

def betweenVar(a, b, c):
    return (a.x-b.x)*(c.x-b.x)+(a.y-b.y)*(c.y-b.y)<0

# class CHull
class CHull:
    def __init__(self, vp):
        self.n = len(vp)
        self.vp = vp
        self.isConvex = False
        self.diam = 0
	
    def convexify(self):
        pass

    def diameter(self):
        if self.diam == 0:
            self.xmin = self.vp[0].x
            self.xmax = self.xmin
            self.ymin = self.vp[0].y
            self.ymax = self.ymin
            for p in self.vp:
                if p.x < self.xmin:
                    self.xmin = p.x
                if p.x > self.xmax:
                    self.xmax = p.x
                if p.y < self.ymin:
                    self.ymin = p.y
                if p.y > self.ymax:
                    self.ymax = p.y
                self.diam = min(self.xmax-self.xmin, self.ymax-self.ymin)
	
# class Bezier
class Bezier(CHull):
    def __init__(self, v):
        self.deg = len(v) - 1
        self.cp = v
        self.tmin = NT(0)
        self.tmax = NT(1)
	
    def getPoint(self, t):
        curr = [0]*self.deg
        # get initial
        for i in range(self.deg):
            curr[i] = self.cp[i].towards(self.cp[i+1], t)
        for i in range(self.deg-1):
            for j in range(self.deg-1-i):
                curr[j] = curr[j].towards(curr[j+1], t)
        return curr[0]

    def subdivision(self, t):
        lseq = [0]*(self.deg+1)
        rseq = [0]*(self.deg+1)
        curr = [0.0]*self.deg

        lseq[0] = self.cp[0]
        rseq[self.deg] = self.cp[self.deg]
        for i in range(self.deg):
            curr[i] = self.cp[i].towards(self.cp[i+1], t)
        for i in range(self.deg-1):
            lseq[i+1] = curr[0]
            rseq[self.deg-i-1] = curr[self.deg-i-1]
            for j in range(self.deg-1-i):
                curr[j] = curr[j].towards(curr[j+1], t)
                lseq[self.deg] = curr[0]
                rseq[0] = curr[0]
                
                return [lseq, rseq]

def plotCP(cp):
    x = []; y = []
    for i in range(len(cp)):
        x.append(cp[i].x)
        y.append(cp[i].y)
    plt.plot(x, y)
    
def plotBezier(bezier, n):
    eps = NT(1)/n
    x = []
    y = []
	
    t = 0
    for i in range(n+1):
        p = bezier.getPoint(t)
        t = t + eps
        x.append(p.x)
        y.append(p.y)
	
    plt.plot(x, y)

def pt(x, y):
    return Point(NT(x), NT(y))

def demo():
    #vp = [pt(0, 0), pt(0.2, 1), pt(1, 1), pt(1, 0.2), pt(2, 0.2), pt(2, 1)]
    #this next curve has a singularity:
    vp = [pt(0,0), pt(1,0), pt(.5, -.5), pt(.5, .5)]
        
    bc = Bezier(vp)

    plotCP(vp)
    plotBezier(bc, 100)
	
    plt.show()

def demoSubdivision():
    vp = [pt(0, 0), pt(0.2, 1), pt(1, 1), pt(1, 0.2), pt(2, 0.2), pt(2, 1)]
	
    bc = Bezier(vp)
    [left, right] = bc.subdivision(0.4)
    print("left=", left)
    print("right=", right)

    # plot original
    plotCP(vp)
     
    print("left type: ", type(left))
    print("right type: ", type(right))
    
    # plot left
    #plotCP(left)
    #plotBezier(Bezier(left), 100)
	
    # plot left
    #plotCP(right)
    #plotBezier(Bezier(right), 100)

    plt.show()

if __name__ == "__main__":
    # demoSubdivision()
    demo()
    demoSubdivision()

    