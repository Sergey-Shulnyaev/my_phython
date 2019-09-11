# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:33:20 2019

@author: mag
"""

my_arr = [1, 2, [3, [4, 5]], 6]


def my_flatten(arr, res = None):
    if res == None:
        res = []
    """
    >>> print(my_flatten([1, 2, [3, [4, 5]], 6]))
    [1, 2, [3, [4, 5]], 6]
    >>> print(my_flatten([1, 2, [3, [4, 5]], 6]))
    [1, 2, [3, [4, 5]], 6]
    """
    for item in arr:
        if type(item) == int:
            res.append(item)
        else:
            my_flatten(item, res)
    return res

print(my_flatten([1, 2, [3, [4, 5]], 6]))
print(my_flatten([1, 2, [3, [4, 5]], 6]))