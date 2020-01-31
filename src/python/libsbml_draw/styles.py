# module intended to provide out of the box styles for config option in SBMLLayout


class _AttributeSet:
    """
    A base class for an immutable dictionary. Subclasses
    are intended to be used as dictionaries to hold keyword
    arguments.

    Only attributes that are present as class attributes
    may be accessed either by dot notation `'.' or get
    notation `dct['x']`. Attempts to add new items will cause
    errors, with information about which attributes the dictionary
    is allowed to take.

    .. code-block

        class Items(_AttributeSet):
            pen='blue'
            size=20

    >>> items = Items()
    >>> items['size']
    20
    >>> items.size
    20
    >>> items['pencil'] # oops

    """
    # subclasses must implement their own _func_map and target_list
    _func_map = dict(
        target=None)  # a map between uable pythonic names for attributes and method that will set the attribute

    def __init__(self):
        if not hasattr(self, '_func_map'):
            raise AttributeError('A _func_map attribute is required but could not ]'
                                 'be found in object of type {}'.format(self.__class__.__name__))
        if 'target' not in self._func_map.keys():
            raise AttributeError("The _func_map dict must contain a 'target' "
                                 "key which has a value corresponding to "
                                 "the method that gets the targets of "
                                 "the current _ArgumentSet. For example, the Node "
                                 "_ArgumentSet would contain 'getNodeIds'.")
        self.__dict__ = {k: v for k, v in self.__class__.__dict__.items() if not k.startswith('__') or callable(v)}

    def _error_message(self, k):
        return f'Key "{k}" is not a valid key ' \
            f'for {self.__class__.__name__}. These are ' \
            f'valid keys: "{list(self.__dict__.keys())}"'

    def __setitem__(self, key, value):
        if key not in self.__dict__.keys():
            raise TypeError(self._error_message(key))
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __delitem__(self, key):
        NotImplemented("Cannot add or remove entries from a _AttributeSet")

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def set_values(self, sbml_layout):
        """
        generic method for setting attributes using the settings ValidatedDict.
        Args:
            vdict: a validated dict,
            attribute:

        Returns:

        """
        for k, v in self.items():
            # exclude _func_dict and target
            if not k.startswith('_') and k != 'target':
                func = getattr(sbml_layout, self._func_map[k])
                assert callable(func)
                target_func = getattr(sbml_layout, self._func_map['target'])
                assert callable(target_func)
                [func(i, v) for i in target_func()]


class _Font(_AttributeSet):
    color = '#000000'
    family = 'Arial'
    name = 'Arial'
    size = 20
    style = 'normal'
    weight = 'normal'

    _func_map = dict(
        color='setNodeFontColor',
        family='setNodeFontFamily',
        name='setNodeFontName',
        size='setNodeFontSize',
        style='setNodeFontStyle',
        weight='setNodeFontWeight',
        target='getNodeIds'
    )


class _Node(_AttributeSet):
    color = r'#c9e0fb'
    edgecolor = r'#0000ff'
    edgewidth = 3
    fillcolor = r'#c9e0fb'

    _func_map = dict(
        color='setNodeColor',
        edgecolor='setNodeEdgeColor',
        edgewidth='setNodeEdgeWidth',
        fillcolor='setNodeFillColor',
        height='setNodeHeight',
        width='setNodeWidth',
        target='getNodeIds'
    )


class _Edge(_AttributeSet):
    width = 3
    color = '#0000ff'

    _func_map = dict(
        width='setReactionCurveWidth',
        color='setReactionEdgeColor',
        target='getReactionIds'
    )


class _Compartments(_AttributeSet):
    edgecolor = '#0000ff30'
    fillcolor = '#0000ff05'
    linewidth = 10

    _func_map = dict(
        edgecolor='setCompartmentEdgeColor',
        fillcolor='setCompartmentFillColor',
        linewidth='setCompartmentLineWidth',
        target='getCompartmentIds'
    )


class Style(_AttributeSet):
    """
    Store aesthetic preference options and pass
    them to :py:class:`sbml_layout.SBMLlayout`

    A Style has four main characteristics that
    can be changed: edge, node, compartment and font. These
    attributes themselves have the following attributes:

    - font:
        - color
        - family
        - name
        - size
        - style
        - weight
    - node
        - color
        - edgecolor
        - edgewidth
        - fillcolor
    - edge
        - edgecolor
        - fillcolor
        - linewidth
    - compartment
        - edgecolor
        - fillcolor
        - linewidth
    """
    node = _Node()
    font = _Font()
    compartment = _Compartments()
    edge = _Edge()  # applied to all edges



def black_and_white():
    """
    Preset black and white style
    Returns:

    """
    s = Style()
    s.compartment.edgecolor = '#c4c4c4ff'
    s.edge.color = 'black'
    s.node.edgecolor = 'black'
    s.node.fillcolor = 'white'
    s.compartment.fillcolor = 'white'
    s.node.edgewidth = 10
    s.font.size = 25
    s.edge.width = 5
    return s




