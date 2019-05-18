import tellurium as te
import libsbml_draw as SBMLlayout

r = te.loada('''
// Reactions:
J0: Node8_Long_Name + Node5 => Node9; J0_kNode8_Long_NameNode5;
J1: Node11 + Node9 => Node14; J1_kNode11Node9;
J2: Node0 + Node13 => Node7 + Node12; J2_kNode0Node13;
J3: Node0 => Node13; J3_kNode0;
J4: Node8_Long_Name + Node14 => Node6; J4_kNode8_Long_NameNode14;
J5: Node12 + Node5 => Node13 + Node0; J5_kNode12Node5;
J6: Node0 + Node3 => Node8_Long_Name; J6_kNode0Node3;
J7: Node10 => Node8_Long_Name; J7_kNode10;

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
s.setReactionCurveWidth ('all', 1)
p = s.drawNetwork(figure_size=(12,10))