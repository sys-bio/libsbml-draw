# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:22:19 2019

@author: nrhaw
"""

import tellurium as te
import roadrunner

r = te.loada("""
   S1 -> S2; k1*S1;
   k1 = 0.1; S1 = 10
""")

