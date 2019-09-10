Sample session in libsbml_draw
--------------------------------

This code example shows how to load an SBML file, draw the model, 
save the figure as a pdf file, and write out the file again as
an SBML file.

.. code-block:: python

    from libsbml_draw import SBMLlayout

    s = SBMLlayout("original_sbml_model.xml")

    s.drawNetwork("my_sbml_model.pdf")

    s.writeSBML("my_sbml_model.xml")