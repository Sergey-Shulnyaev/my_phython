# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

my_arr = [1, 2, [3, [4, 5]], 6]


def my_flatten(arr):
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
            res += my_flatten(item )
    return res

print(my_flatten([1, 2, [3, [4, 5]], 6]))
print(my_flatten([1, 2, [3, [4, 5]], 6]))