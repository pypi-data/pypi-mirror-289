"""The MIT License (MIT).

Copyright (c) 2023 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""
from mypy.nodes import Decorator, FuncDef, TypeAlias, IndexExpr, Var, NameExpr, TypeInfo, FakeInfo
from mypy.types import AnyType

from pyeo.exceptions import FakeInfoDetectedError


class EachMethodHasProtocolFeature(object):
    """Checking each object method has protocol."""

    def analyze(self, ctx) -> bool:
        """Analyzing.

        :param ctx: mypy context
        :return: bool
        """
        object_methods = {
            def_body.name: def_body
            for def_body in ctx.cls.defs.body
            if self._is_public_method(def_body)
        }
        if not ctx.cls.base_type_exprs:
            return False
        extra_method_names = object_methods.keys() - self._protocol_method_names(ctx.cls.base_type_exprs)
        if extra_method_names:
            failed_methods = [
                method
                for method_name, method in object_methods.items()
                if method_name in extra_method_names
            ]
            for method in failed_methods:
                ctx.api.fail(
                    "Class '{0}' have public extra method '{1}' without protocol.".format(
                        ctx.cls.name,
                        method.name,
                    ),
                    method,
                )
        return True

    def _protocol_method_names(self, base_type_exprs):
        res = []
        for base_type in base_type_exprs:
            if isinstance(base_type, IndexExpr):
                node_for_analyze = base_type.base.node
            elif isinstance(base_type.node, Var) and isinstance(base_type.node.info, FakeInfo):
                raise FakeInfoDetectedError
            elif isinstance(base_type.node, TypeAlias):
                if isinstance(base_type.node.target, AnyType):
                    raise FakeInfoDetectedError
                node_for_analyze = base_type.node.target.type
            elif isinstance(base_type.node, TypeInfo):
                for node in base_type.node.mro:
                    for method in node.names:
                        res.append(method)
                continue
                node_for_analyze = base_type.node
            else:
                node_for_analyze = base_type.node
            for node in node_for_analyze.mro:
                if not hasattr(node.defn.info, 'names'):
                    continue
                for method in node.defn.info.names:
                    res.append(method)
        return res

    def _is_public_method(self, def_body):
        is_func_def = isinstance(def_body, FuncDef)
        return is_func_def and not def_body.name.startswith('_') and not self._method_is_ctor(def_body)

    def _method_is_ctor(self, def_body) -> bool:
        if not isinstance(def_body, Decorator):
            return False
        for dec in def_body.original_decorators:
            if dec.name == 'classmethod':
                return True
        return False
