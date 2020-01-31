####################
Example using Styles
####################

:py:class:`styles.Style` provide a higher level mechanism for controlling
figure aesthetics. You can use a preconfigured style or configure your own.

Preconfigured styles
--------------------

    * black_and_white

Example of using a preconfigured style:

.. code-block:: python

    import os
    from libsbml_draw import SBMLlayout
    from libsbml_draw.styles import Style, black_and_white

    model_id = 'BIOMD0000000096'

    fname = model_id + '.xml'

    # download the model
    biomodels_download(model_id, fname)

    # Use a preconfigured style directly out of the box
    s = SBMLlayout(fname, style=black_and_white)

    # draw the network
    s.drawNetwork(model_id + ".png")

    # write the newly generated layout and rendering information back to the
    # sbml model
    s.writeSBML(fname)

An example of creating your own style:


.. code-block:: python

    import os
    from libsbml_draw import SBMLlayout
    from libsbml_draw.styles import Style, black_and_white

    def my_style():
        s = Style()
        s.node.color = 'green'
        s.node.edgewidth = 4
        s.font.color = 'red'
        s.font.size = 25
        s.edge.color = 'black'
        s.compartment.edgecolor = 'black
        return s

    model_id = 'BIOMD0000000096'

    fname = model_id + '.xml'

    # download the model
    biomodels_download(model_id, fname)

    # Use a preconfigured style directly out of the box
    s = SBMLlayout(fname, style=my_style)

    # draw the network
    s.drawNetwork(model_id + ".png")

    # write the newly generated layout and rendering information back to the
    # sbml model
    s.writeSBML(fname)












