# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FunctionCall(Component):
    """A FunctionCall component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- docs (a list of or a singular dash component, string or number; optional)

- inputs (a list of or a singular dash component, string or number; optional)

- outputs (a list of or a singular dash component, string or number; optional)"""
    _children_props = ['inputs', 'outputs', 'docs']
    _base_nodes = ['inputs', 'outputs', 'docs', 'children']
    _namespace = 'dongjak_dash_components2'
    _type = 'FunctionCall'
    @_explicitize_args
    def __init__(self, children=None, inputs=Component.UNDEFINED, outputs=Component.UNDEFINED, docs=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'docs', 'inputs', 'outputs']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'docs', 'inputs', 'outputs']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FunctionCall, self).__init__(children=children, **args)
