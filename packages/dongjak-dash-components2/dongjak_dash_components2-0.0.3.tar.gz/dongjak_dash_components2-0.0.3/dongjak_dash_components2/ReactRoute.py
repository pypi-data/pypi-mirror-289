# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ReactRoute(Component):
    """A ReactRoute component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- Component (boolean | number | string | dict | list; optional)

- ErrorBoundary (boolean | number | string | dict | list; optional)

- HydrateFallback (boolean | number | string | dict | list; optional)

- action (boolean | number | string | dict | list; optional)

- caseSensitive (boolean; optional)

- element (a list of or a singular dash component, string or number; optional)

- errorElement (a list of or a singular dash component, string or number; optional)

- handle (boolean | number | string | dict | list; optional)

- hasErrorBoundary (boolean; optional)

- hydrateFallbackElement (a list of or a singular dash component, string or number; optional)

- icon (a list of or a singular dash component, string or number; optional)

- index (boolean; optional)

- lazy (boolean | number | string | dict | list; optional)

- loader (boolean | number | string | dict | list; optional)

- path (string; optional)

- shouldRevalidate (dict; optional)

    `shouldRevalidate` is a dict with keys:
"""
    _children_props = ['icon', 'element', 'hydrateFallbackElement', 'errorElement']
    _base_nodes = ['icon', 'element', 'hydrateFallbackElement', 'errorElement', 'children']
    _namespace = 'dongjak_dash_components2'
    _type = 'ReactRoute'
    @_explicitize_args
    def __init__(self, children=None, icon=Component.UNDEFINED, caseSensitive=Component.UNDEFINED, path=Component.UNDEFINED, id=Component.UNDEFINED, lazy=Component.UNDEFINED, loader=Component.UNDEFINED, action=Component.UNDEFINED, hasErrorBoundary=Component.UNDEFINED, shouldRevalidate=Component.UNDEFINED, handle=Component.UNDEFINED, index=Component.UNDEFINED, element=Component.UNDEFINED, hydrateFallbackElement=Component.UNDEFINED, errorElement=Component.UNDEFINED, Component=Component.UNDEFINED, HydrateFallback=Component.UNDEFINED, ErrorBoundary=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'Component', 'ErrorBoundary', 'HydrateFallback', 'action', 'caseSensitive', 'element', 'errorElement', 'handle', 'hasErrorBoundary', 'hydrateFallbackElement', 'icon', 'index', 'lazy', 'loader', 'path', 'shouldRevalidate']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'Component', 'ErrorBoundary', 'HydrateFallback', 'action', 'caseSensitive', 'element', 'errorElement', 'handle', 'hasErrorBoundary', 'hydrateFallbackElement', 'icon', 'index', 'lazy', 'loader', 'path', 'shouldRevalidate']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ReactRoute, self).__init__(children=children, **args)
