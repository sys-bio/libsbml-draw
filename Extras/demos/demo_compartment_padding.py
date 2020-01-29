import tellurium as te
import roadrunner
import libsbml_draw as SBMLlayout

r = te.loada("""
   compartment VOL;
   species A in VOL, B in VOL, C in VOL;
   
   A -> B; k1*A;
   B -> C; k2*B;
   k1 = 0.1; k2 = 0.2;
""")

s = SBMLlayout.SBMLlayout(r.getSBML())

s.describeModel()

s.drawNetwork()


s.setLayoutAlgorithmOptions(padding=40)

s.regenerateLayout()

s.drawNetwork()

