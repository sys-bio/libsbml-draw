# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:04:56 2019

@author: nrhaw
"""

import tellurium as te
import roadrunner

r = te.loada("""
    ABCDEFG -> B; k1*ABCDEFG;
    B -> C + D; k1*B;
    C -> ABCDEFG; k3*C;
    C -> D + E; k4*C;
    D + B -> F; k5*D+B;
    
    k1 = 1; k2 = 1; k3 = 1; k4 = 1; k5 = 2
""")

te.saveToFile ('c:\\tmp\\largerpathway.xml', r.getSBML())
