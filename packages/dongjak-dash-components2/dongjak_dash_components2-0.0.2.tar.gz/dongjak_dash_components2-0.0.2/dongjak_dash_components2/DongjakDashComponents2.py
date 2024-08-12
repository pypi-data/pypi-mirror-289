# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DongjakDashComponents2(Component):
    """A DongjakDashComponents2 component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- test (a list of or a singular dash component, string or number; required)"""
    _children_props = ['test']
    _base_nodes = ['test', 'children']
    _namespace = 'dongjak_dash_components2'
    _type = 'DongjakDashComponents2'
    @_explicitize_args
    def __init__(self, test=Component.REQUIRED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'test']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'test']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['test']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DongjakDashComponents2, self).__init__(**args)
