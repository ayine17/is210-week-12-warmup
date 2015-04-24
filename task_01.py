#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """function so that attempts to access any index or key of var1 that do not
       exist will print a warning message and return var1
    args:
        var1[list]: list use for the eception testing
        var2[int]: int use to access the index or keys of Var1
    return:
        return var1

    Example:

        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        [1,2]
        >>> simple_lookup({}, 'banana')
        Warning: Your index/key doesn't exist.
        {}
    """
    try:
        return var1[var2]

    except LookupError:
        print "Warning: Your index/key doesn't exist."
    return var1
