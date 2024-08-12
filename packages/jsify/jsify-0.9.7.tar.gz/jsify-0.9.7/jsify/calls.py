"""
The `calls` module provides a decorator that facilitates the handling of JSON-like data structures within Python
functions. This module is particularly useful for developers working with data in the form of dictionaries, lists,
and tuples, as it simplifies the conversion of these data structures into `Object` instances, enabling
attribute-style access and other JSON-like behaviors.
At the heart of this module is the `jsified_function` decorator, which automatically converts function arguments into
`Object` instances. Additionally, the decorator offers options to process the function's return value, allowing it
to be returned in its original form or as a deeply unjsified structure, depending on the specified flags.
"""

from .jsify import unjsify, Object, deep_unjsify
from .stringcase import json_camel_to_snake


def jsified_function(*args, result_original=False, result_deep_original=False):
    """
    A decorator to convert function arguments to `Object` and process the results accordingly.

    This decorator can be applied to a function to ensure that its arguments are automatically
    converted to `Object` instances if they are of types `dict`, `list`, or `tuple`. It also
    processes the function's result based on the provided flags.

    Parameters
    ----------
    *args : tuple
        Positional arguments that may include the function to be decorated.
    result_original : bool, optional
        If True, the function's result will be unjsified using `unjsify`. Default is False.
    result_deep_original : bool, optional
        If True, the function's result will be deeply unjsified using `deep_unjsify`. Default is False.

    Returns
    -------
    function
        The decorated function with arguments converted to `Object` and results processed based on the flags.
    """
    def create_decorator():
        def decorator(function):
            def wrapper(*wrapper_args, **kwargs):
                def conditional_json_object(o):
                    return Object(o) if isinstance(o, (dict, list, tuple)) else o
                json_args = list(map(lambda a: conditional_json_object(a), wrapper_args))
                json_kwargs = dict(map(lambda item: (item[0], conditional_json_object(item[1])), kwargs.items()))
                result = function(*json_args, **json_kwargs)
                return deep_unjsify(result) if result_deep_original \
                    else unjsify(result) if result_original \
                    else Object(result)
            return wrapper
        return decorator
    if len(args):
        return create_decorator()(function=args[0])
    else:
        return create_decorator()


def camelized_function(*args, replace=None):
    """
    A decorator to convert the keys of JSON-like dictionaries from camelCase to snake_case before passing them to the
    function.

    Parameters
    ----------
    replace : dict, optional
        A dictionary to specify replacements for certain keys after conversion to snake_case.

    Returns
    -------
    function
        A decorator that applies the conversion to the decorated function's keyword arguments.
    """
    def wrapper_with_parameters(func):
        def wrapper(**kwargs):
            return func(**json_camel_to_snake(kwargs, replace=replace))
        return wrapper
    return wrapper_with_parameters if len(args) == 0 else wrapper_with_parameters(args[0])


def json_function(f):
    """
    A decorator that allows a function to accept a JSON dictionary via a special `_json` keyword argument.

    This decorator checks if the `_json` keyword argument is provided. If it is, the dictionary passed via `_json`
    is unpacked and its key-value pairs are added to the function's keyword arguments before the function is called.

    :param f: The function to be decorated.
    :type f: function
    :return: The decorated function.
    :rtype: function
    """
    def wrapper(*args, **kwargs):
        if "_json" in kwargs:
            json_args = kwargs.pop("_json")
            kwargs.update(json_args)
        return f(*args, **kwargs)
    return wrapper
