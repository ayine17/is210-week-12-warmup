#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """error"""
    pass


def get_age(birthyear):

    """function calcute age

    args:
        birthyear(mix): year of birth
    return:
        age(int): return int age if age is zero or greater or
                  raise a InvalidAgeError

    example:
        >>> get_age(2004)
        11
        >>> get_age(2014)
        1
        >>> get_age(2499)

        Traceback (most recent call last):
        File "<pyshell#2>", line 1, in <module>
        get_age(2499)
        raise InvalidAgeError
        InvalidAgeError
    """

    age = datetime.datetime.now().year - birthyear

    if age >= 0:
        return age
    else:
        raise InvalidAgeError
