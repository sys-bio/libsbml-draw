import tellurium as te
import libsbml_draw as SBMLlayout

r = te.loada('''
// Reactions:
J0: Node8_Long_Name + Node5 => Node9; J0_k;
J1: Node11 + Node9 => Node14; J1_k;
J2: Node0 + Node13 => Node7 + Node12; J2_k;
J3: Node0 => Node13; J3_k;
J4: Node8_Long_Name + Node14 => Node6; J4_k;
J5: Node12 + Node5 => Node13 + Node0; J5_k;
J6: Node0 + Node3 => Node8_Long_Name; J6_k;
J7: Node10 => Node8_Long_Name; J7_k;

// Variable initializations:
J0_k = 0.1;
J1_k = 0.1;
J2_k = 0.1;
J3_k = 0.1;
J4_k = 0.1;
J5_k = 0.1;
J6_k = 0.1;
J7_k = 0.1;
''')

s = SBMLlayout.SBMLlayout (r.getSBML())
s.drawNetwork(figsize=(14,14))
s.drawNetwork(figsize=(10,10))