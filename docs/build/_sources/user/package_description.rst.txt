Summary of libsbml_draw 
--------------------------------

Purpose
^^^^^^^^

The SBML layout and render extensions enable SBML models to encode 
information about the graphical depiction of model elements.  
Layout provides information about the positions of model elements 
and render describes the styles of elements, for example, shapes, 
colors, line widths, and font details.  

libsbml_draw supports the SBML layout and render extensions and can 
automatically generate a layout for SBML models by making use of SBNW, 
a C/C++ library. 

Code
^^^^^

``libsbml-draw`` provides one Python class, ``SBMLlayout``, for the user to access 
all methods available for working with SBML models.  This is the only entry point 
into libsbml-draw for the user.

Via methods provided by ``SBMLlayout``, the user can load a model file, 
draw a model, change render attributes, and write out a model as an SBML file.

