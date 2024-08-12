# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AdminAppLayout(Component):
    """An AdminAppLayout component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- routes (list of dicts; optional)

    `routes` is a list of dicts with keys:

    - children (list of boolean

      Or number | string | dict | lists; optional)

    - icon (a list of or a singular dash component, string or number; optional)

    - label (string; required) | dict with keys:

    - element (a list of or a singular dash component, string or number; optional)

    - path (string; optional)"""
    _children_props = ['routes[].icon', 'routes[].element']
    _base_nodes = ['children']
    _namespace = 'dongjak_dash_components2'
    _type = 'AdminAppLayout'
    @_explicitize_args
    def __init__(self, children=None, routes=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'routes']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'routes']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(AdminAppLayout, self).__init__(children=children, **args)
