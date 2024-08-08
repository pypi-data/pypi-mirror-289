# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class UsernamePasswordLogin(Component):
    """An UsernamePasswordLogin component.


Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowsForgotPassword (boolean; optional):
    允许找回密码.

- allowsSignup (boolean; optional):
    是否允许用户注册.

- aria-* (string; optional):
    Wild card aria attributes.

- data-* (string; optional):
    Wild card data attributes.

- loginUrl (string; required):
    登录链接.

- tabIndex (number; optional):
    tab-index.

- usernameType (a value equal to: 'email', 'username'; optional):
    用户名类型.

- welcomeMessage (string; optional):
    在表单上方显示的消息."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dongjak_dash_components'
    _type = 'UsernamePasswordLogin'
    @_explicitize_args
    def __init__(self, loginUrl=Component.REQUIRED, welcomeMessage=Component.UNDEFINED, allowsSignup=Component.UNDEFINED, usernameType=Component.UNDEFINED, allowsForgotPassword=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowsForgotPassword', 'allowsSignup', 'aria-*', 'data-*', 'loginUrl', 'tabIndex', 'usernameType', 'welcomeMessage']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowsForgotPassword', 'allowsSignup', 'aria-*', 'data-*', 'loginUrl', 'tabIndex', 'usernameType', 'welcomeMessage']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['loginUrl']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(UsernamePasswordLogin, self).__init__(**args)
