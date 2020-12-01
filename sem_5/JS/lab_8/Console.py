#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import sys
import time


class _RangeError(Exception): pass


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80,
               force_lower=False):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{0} must have at least {1} and "
                        "at most {2} characters".format(
                        name, minimum_length, maximum_length))
            return line if not force_lower else line.lower()
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=None,
                maximum=None, allow_zero=True):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            x = int(line)
            if x == 0:
                if allow_zero:
                    return x
                else:
                    raise _RangeError("{0} may not be 0".format(name))
            if ((minimum is not None and minimum > x) or 
                (maximum is not None and maximum < x)):
                raise _RangeError("{0} must be between {1} and {2} "
                        "inclusive{3}".format(name, minimum, maximum,
                        (" (or 0)" if allow_zero else "")))
            return x
        except _RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


def get_float(message, name="float", default=None, minimum=None,
              maximum=None, allow_zero=True):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            x = float(line)
            if abs(x) < sys.float_info.epsilon:
                if allow_zero:
                    return x
                else:
                    raise _RangeError("{0} may not be 0.0".format(
                                      name))
            if ((minimum is not None and minimum > x) or 
                (maximum is not None and maximum < x)):
                raise _RangeError("{0} must be between {1} and {2} "
                        "inclusive{3}".format(name, minimum, maximum,
                        (" (or 0.0)" if allow_zero else "")))
            return x
        except _RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be a float".format(name))


def get_bool(message, default=None):
    yes = frozenset({"1", "y", "yes", "t", "true", "ok","tak"})
    message += " (y/yes/n/no)"
    message += ": " if default is None else " [{0}]: ".format(default)
    line = input(message)
    if not line and default is not None:
        return default in yes
    return line.lower() in yes


def get_date_GB(message, default=None, forma="%y-%m-%d"):
    # message should include the format in human-readable form, e.g.
    # for %y-%m-%d, "YY-MM-DD".
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            return time.strptime(line, forma)
            #return datetime.datetime.strptime(line, forma)
        except ValueError as err:
            print("ERROR", err)

def get_date(message, default=None, forma="%y-%m-%d"):
    # message should include the format in human-readable form, e.g.
    # for %y-%m-%d, "YY-MM-DD".
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            return time.strptime(line, forma)
            #return datetime.datetime.strptime(line, forma)
        except ValueError as err:
            print("ERROR", err)


def get_menu_choice(message, valid, default=None, force_lower=False):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        line = input(message)
        if not line and default is not None:
            return default
        if line not in valid:
            print("ERROR only {0} are valid choices".format(
                  ", ".join(["'{0}'".format(x)
                  for x in sorted(valid)])))
        else:
            return line if not force_lower else line.lower()


'''
sys.float_info: difference between 1.0 and the least value greater than 1.0 that is 
representable as a float
'''
       
       
def equal_float(a, b, decimals=None):
    """Returns True if a and b are equal to the limits of the machine's
    accuracy or to the specified number of decimal places if specified

    >>> equal_float(.1, .1), equal_float(.000000000001, .000000000001)
    (True, True)
    >>> equal_float(.00000000000101, .00000000000102, 13)
    True
    >>> equal_float(.00000000000101, .00000000000102)
    False
    >>> equal_float(.00000000000101, .00000000000102, 9)
    True
    """
    if decimals is not None:
        a = round(a, decimals)
        b = round(b, decimals)
    return abs(a - b) <= (sys.float_info.epsilon * min(abs(a), abs(b)))


filename=""
key=""
data= {}


import shelve

d = shelve.open(filename)  # open -- file may get suffix added by low-level
                        # library
d[key] = data              # store data at key (overwrites old data if
                        # using an existing key)
data = d[key]              # retrieve a COPY of data at key (raise KeyError
                        # if no such key)
del d[key]                 # delete data stored at key (raises KeyError
                        # if no such key)
flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = [0, 1, 2]        # this works as expected, but...
d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']             # extracts the copy
temp.append(5)             # mutates the copy
d['xx'] = temp             # stores the copy right back, to persist it

# or, d=shelve.open(filename,writeback=True) would let you just code
# d['xx'].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it
