from libsbml_draw.sbml_layout import SBMLlayout

'''

add a config argument to SBMLlayout. 
This is either nested dict or yaml string or fname.
Helper methods for generating the position dictionary

Create another module called styles, with ready importable
preconfigured styles
'''

fname = f'Schmierer2008.xml'

s = SBMLlayout(fname)
font = dict()
s.drawNetwork(
    save_file_name='network.png',
    show=True, dpi=300, width_shift=0.25,
    height_shift=0.25, scaling_factor=1
)
s.regenerateLayout()
s.drawNetwork()
# s.writeSBMLFile("Schmierer2008WithLayout.xml")
'''
# node attributes

# edge attributes
ArrowheadNumStyles
ArrowheadNumVerts
ArrowheadStyle
ArrowheadScale
ArrowheadVert

'''
# create a validated dictionary type which behves like a dict
# that can only have certain keys



node_dict = dict(
        font=dict(
            fontsize=18,
            fontstyle='Arial',
            NodeFontColor=0,
            NodeFontFamily=0,
            NodeFontName=0,
            NodeFontSize=0,
            NodeFontStyle=0,
            NodeFontWeight=0
        ),
        shape=dict(
            aliasNodes=[],
            NodeCentroid=0,
            NodeColor=0,
            NodeEdgeColor=0,
            NodeEdgeWidth=0,
            NodeFillColor=0,
            NodeHeight=0,
            NodeWidth=0,
            NodeLowerLeftPoint=0
        ),
        position=dict(
            NodeTextAnchor=0,
            VNodeTextAnchor=0
        )
)
settings = dict(
    nodes=node_dict,
        reactants=dict(), # another node_dict
        # NumberOfRoles=0,  # todo have rolecolor for reactants, products and modifiers (boundary conditions?)
        # IsNodeAliased=0,  # todo have a list for alias
        # IsNodeLocked=0,  # todo list for locked nodes
    ),
    edges=dict(
        ReactionIds=0,
        ReactionBezierPoints2=0,
        ReactionCentroid=0,
        ReactionCurveWidth=0,
        ReactionEdgeColor=0,
        ReactionFillColor=0,
        CompartmentIds=0,
    ),
    compartments=dict(
        NumberOfCompartments=0,
        CompartmentEdgeColor=0,
        CompartmentFillColor=0,
        CompartmentLineWidth=0,
        LayoutAlgorithmOptions=0,
        NetworkBackgroundColor=0,

    )
)
